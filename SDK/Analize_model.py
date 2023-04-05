# Librerias
import json
import os
import jsonlint
from dotenv import load_dotenv
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.storage.blob import BlobServiceClient, BlobClient
from json_parsing_sdk import function_json_parsing  # Llamamos a la fuction_json_parsing

# Carga las variables de entorno desde el archivo .env
load_dotenv()

endpoint = os.getenv("AZURE_FORM_RECOGNIZER_ENDPOINT")
key = os.getenv("AZURE_FORM_RECOGNIZER_KEY")
model_id = "Model_template"
formUrl = "https://github.com/aratan/Azure-OCR/blob/adfe9d0db7be28cda624e9ea1370d84a67779627/parte_amistoso_0.jpg?raw=true"

document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Make sure your document's type is included in the list of document types the custom model can analyze
poller = document_analysis_client.begin_analyze_document_from_url(model_id, formUrl)
result = poller.result()
'''
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
'''
n = 0;
diccionario = {}

for document in result.documents:
    n += 1
    for name, field in document.fields.items():
        # field_value = field.value if field.value else field.content
        field_value = field.content
        # convertir el valor a una cadena si no es una cadena
        if not isinstance(field_value, str):
            field_value = str(field_value)
        diccionario[name] = field_value

try:
    data = jsonlint.ValidationError(diccionario)
    print("\n El JSON es válido/reparado:", data)


except json.JSONDecodeError as err:
    print("\n El JSON no es válido:" + str(err))



# Nombrar el archivo JSON generado con el nombre del archivo de imagen de entrada
output_filename = f"{name}.json"
with open(output_filename, "w") as archivo_json:
    json.dump(diccionario, archivo_json, ensure_ascii=False, sort_keys=True, indent=4 )


# Llamamos a la function para realizar el parseo
function_json_parsing(diccionario)

