import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Se establece la cadena de conexión a la cuenta de almacenamiento
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

# Crea el  BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Crea un nombre unico para el contenedor
container_name = "prueba"
# Crea el contenedor en la cuenta de almacenamiento
container_client = blob_service_client.create_container(container_name)

# Se especifica la ruta de la carpeta que contiene las imágenes a subir
folder_path = "/sysroot/home/andreasandoval/Documentos/BOOTCAMP_F5/OCR/OCR_Capgemini/SDK/Renombrar/jsons_10"

# Se imprime el mensaje de confirmación
print(f"El contenedor {container_name} se ha creado correctamente.")

# Se itera sobre cada archivo en la carpeta especificada y se sube al contenedor
for filename in os.listdir(folder_path):
    # Se crea el BlobClient para el archivo actual
    blob_client = container_client.get_blob_client(filename)

    # Se sube el archivo al contenedor
    with open(os.path.join(folder_path, filename), "rb") as data:
        blob_client.upload_blob(data)

    # Se imprime el mensaje de confirmación
    print(f"La imagen {filename} se ha subido correctamente.")