#Importación de librerías
import os
import jsonlint
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, redirect, json
from azure.ai.formrecognizer import DocumentModelAdministrationClient
from azure.core.credentials import AzureKeyCredential
from werkzeug.utils import secure_filename
from azure.ai.formrecognizer import DocumentAnalysisClient

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Configurar el cliente de Form Recognizer
endpoint = os.getenv("AZURE_FORM_RECOGNIZER_ENDPOINT")
key = os.getenv("AZURE_FORM_RECOGNIZER_KEY")
model_id = "model_1"

credential = AzureKeyCredential(key)
document_model_admin_client = DocumentModelAdministrationClient(endpoint, credential)

# Crear una instancia del framework Flask
app = Flask(__name__)

# Definir la ruta de la carpeta de subida
app.config['UPLOAD_FOLDER'] = '/sysroot/home/andreasandoval/Documentos/BOOTCAMP_F5/OCR/OCR_Capgemini/API/Images'

#Se define la ruta de inicio
@app.route('/')
def hello():
    return render_template("main.html")

# Definir la ruta para procesar la imagen y devolver el archivo JSON
@app.route('/analize_image', methods=['POST'])
def subir_imagen():

    if request.method == 'POST':

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
        # Crear un diccionario con los datos que quieres incluir en el JSON
        json_data = {
            "doc_type": document.doc_type,
            "confidence": document.confidence,
            "fields": {name: field.value if field.value else field.content for name, field in document.fields.items()}
        }

        # Convertir el diccionario en un objeto JSON con formato legible
        pretty_json = json.dumps(json_data, indent=4)

        # Enviar el JSON como respuesta
        return jsonify(pretty_json)

if __name__ == "__main__":
    app.run()