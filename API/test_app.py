import json
import os
import tempfile
import pytest
from app import app
from bs4 import BeautifulSoup

def test_hello():
    client = app.test_client()

    # Simular una solicitud GET a la ruta "/"
    response = client.get('/')

    # Verificar que la respuesta tenga un status code 200 OK
    assert response.status_code == 200

    # Verificar que la plantilla "main.html" se renderice correctamente
    assert b'<!DOCTYPE html>' in response.data


def test_subir_imagen():
    client = app.test_client()

    # Cargar la imagen de prueba
    image_path = os.path.join(os.path.dirname(__file__), 'test_img.jpg')

    # Simular una solicitud POST a la ruta "/analize_image" con el archivo de prueba como datos adjuntos
    with open(image_path, 'rb') as f:
        response = client.post('/analize_image', data={'userfile': (f, 'test_img.jpg')}, content_type='multipart/form-data')

    # Verificar que la respuesta tenga un status code 200 OK
    assert response.status_code == 200

    # Verificar que la plantilla "result.html" se renderice correctamente
    soup = BeautifulSoup(response.data, 'html.parser')
    assert soup.find('div', {'id': 'json_data'}) is not None

    # Obtener el JSON serializado del HTML
    json_str = soup.find('div', {'id': 'json_data'}).text

    # Cargar el JSON
    data = json.loads(json_str)
