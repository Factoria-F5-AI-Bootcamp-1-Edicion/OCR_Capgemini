import json
import os
from dotenv import load_dotenv
from azure.ai.formrecognizer import DocumentModelAdministrationClient
from azure.core.credentials import AzureKeyCredential


# Carga las variables de entorno desde el archivo .env
load_dotenv()


def sample_build_model():
    # [START build_model]

    # Configurar el cliente de Form Recognizer
    endpoint = os.getenv("AZURE_FORM_RECOGNIZER_ENDPOINT")
    key = os.getenv("AZURE_FORM_RECOGNIZER_KEY")
    container_sas_url = os.getenv("CONTAINER_SAS_URL")

    credential = AzureKeyCredential(key)
    document_model_admin_client = DocumentModelAdministrationClient(endpoint, credential)

    #Se crea el modelo
    poller = document_model_admin_client.begin_build_document_model(
        # For more information about build_mode, see: https://aka.ms/azsdk/formrecognizer/buildmode
        build_mode="template", blob_container_url=container_sas_url, model_id="model2_test", description="Nuevas etiquetas"
    )
    model = poller.result()

    print("Model ID: {}".format(model.model_id))
    print("Description: {}".format(model.description))
    print("Model created on: {}\n".format(model.created_on))
    print("Doc types the model can recognize:")
    for name, doc_type in model.doc_types.items():
        print("\nDoc Type: '{}' which has the following fields:".format(name))
        for field_name, confidence in doc_type.field_confidence.items():
            print("Field: '{}' has confidence score {}".format(field_name, confidence))



if __name__ == '__main__':
    sample_build_model()