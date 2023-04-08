#Importación de librerías
import json
import os
import sys
import tempfile
import jsonlint
from dotenv import load_dotenv
from flask import Flask, request, render_template, make_response, send_file
from azure.ai.formrecognizer import DocumentModelAdministrationClient
from azure.core.credentials import AzureKeyCredential
from werkzeug.utils import secure_filename
from azure.ai.formrecognizer import DocumentAnalysisClient


# Agregar la ruta de la carpeta raíz de tu proyecto al sys.path
ruta_actual = sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sdk')))

# Ahora puedes importar funciones desde el paquete sdk
from json_parsing_sdk import function_json_parsing


# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Configurar el cliente de Form Recognizer
endpoint = os.getenv("AZURE_FORM_RECOGNIZER_ENDPOINT")
key = os.getenv("AZURE_FORM_RECOGNIZER_KEY")
model_id = "Model_template"

credential = AzureKeyCredential(key)
document_model_admin_client = DocumentModelAdministrationClient(endpoint, credential)

# Crear una instancia del framework Flask
app = Flask(__name__)

# Definir la ruta de la carpeta de subida
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'Images')


@app.route('/')
def hello():
    return render_template("main.html")

# Definir la ruta para procesar la imagen y devolver el archivo JSON
@app.route('/analize_image', methods=['POST'])
def subir_imagen():
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'Images')

    if request.method == 'POST':

        # Verificar si la carpeta UPLOAD_FOLDER existe, sino crearla
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        f = request.files.get('userfile', None)
        if f is not None:
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            f = request.files['filename']
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)



        with open(image_path, "rb") as f:
            # Make sure your document's type is included in the list of document types the custom model can analyze
            document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))
            poller = document_analysis_client.begin_analyze_document(model_id, document= f)
            result = poller.result()

        for idx, document in enumerate(result.documents):
            print("--------Analyzing document #{}--------".format(idx + 1))
            print("Document has type {}".format(document.doc_type))
            print("Document has confidence {}".format(document.confidence))
            print("Document was analyzed by model with ID {}".format(result.model_id))
            for name, field in document.fields.items():
                field_value = field.value if field.value else field.content
                print("......found field of type '{}' with value '{}' and with confidence {}".format(field.value_type,
                                                                                                     field_value,
                                                                                                     field.confidence))

        n = 0;
        diccionario = {}

        for document in result.documents:
            n += 1
            for name, field in document.fields.items():
                # field_value = field.value if field.value else field.content
                field_value = field.content
                # convertir el valor a una cadena si no es una cadena
                if not isinstance(field_value, str):
                    field_value = json.dumps(field_value, ensure_ascii=False)
                diccionario[name] = field_value

        try:
            data = jsonlint.ValidationError(diccionario)
            #print("\n El JSON es válido/reparado:", data)

        except json.JSONDecodeError as err:
            print("\n El JSON no es válido:" + str(err))

        # Llamamos a la function para realizar el parseo
        data = function_json_parsing(diccionario)

        # Serializar el objeto a JSON con opciones personalizadas
        json_str = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4)

    # Renderizar la plantilla * con el JSON serializado
    return render_template('result.html', json_data=json_str)


# Se define la ruta para descargar el archivo JSON generado
@app.route('/download', methods=['POST'])
def download():
    n = 0;
    n += 1
    json_str = request.form['json_str']
    nombre_archivo = request.form.get('nombre_archivo', f'parte{n}')
    nombre_archivo_json = f"{nombre_archivo}.json"

    # Crear un archivo temporal para almacenar el JSON
    with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as tmp:
        tmp.write(json_str.encode('utf-8'))


    # Crear una respuesta para enviar el archivo
    response = make_response(send_file(tmp.name, as_attachment=True))

    # Establecer las cabeceras para forzar la descarga del archivo
    response.headers['Content-Type'] = 'application/json'
    response.headers['Content-Disposition'] = f'attachment; filename={nombre_archivo_json}'

    return response


if __name__ == '__main__':
    app.run()