import pytest
import unittest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        # Devolver el objeto de cliente para hacer solicitudes HTTP al servidor Flask
        yield client


# Crear una instancia del cliente de pruebas
test_client = app.test_client()


class test_subir_imagen(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = test_client

    def tearDown(self):
        pass

    def test_subir_imagen(self):
        with open('parte_test.jpg', 'rb') as f:
            response = self.app.post('/analize_image',
                                     content_type='multipart/form-data',
                                     data={'userfile': (f, 'parte_test.jpg')})

        self.assertEqual(response.status_code, 200)


def test_main(client):
    # Simular una solicitud GET a la ruta "/"
    response = client.get('/')
    assert response.status_code == 200
    # Verificar que la plantilla "main.html" se renderice correctamente
    assert b'<!DOCTYPE html>' in response.data


def test_download(client):
    # Simulamos una solicitud POST a la ruta '/download' con un archivo JSON
    response = client.post('/download', data={'json_str': '{"doc_type": "Invoice"}'})
    assert response.status_code == 200
    # Verificamos que la respuesta tenga las cabeceras adecuadas para descargar un archivo JSON
    assert response.headers['Content-Type'] == 'application/json'
    assert response.headers['Content-Disposition'] == 'attachment; filename=parte1.json'
