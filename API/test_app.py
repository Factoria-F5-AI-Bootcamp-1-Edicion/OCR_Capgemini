import os
from io import BytesIO
from pytest_mock import mocker
from flask import Flask
from werkzeug.datastructures import FileStorage
from app import subir_imagen

def test_subir_imagen(mocker):
    # Configurar la aplicación Flask
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'tests/images'

    # Cargar una imagen de prueba
    image_path = os.path.join(os.path.dirname(__file__), 'images', 'test_image.png')
    with open(image_path, 'rb') as f:
        file = FileStorage(BytesIO(f.read()), filename='test_image.png')

    # Configurar el objeto mocker para la llamada a Azure Form Recognizer
    mock_poller = mocker.Mock()
    mock_poller.result.return_value = mock_result()
    mock_client = mocker.Mock()
    mock_client.begin_analyze_document.return_value = mock_poller
    mocker.patch('app.DocumentAnalysisClient', return_value=mock_client)

    # Ejecutar la función subir_imagen() con la imagen de prueba
    with app.test_request_context('/analize_image', method='POST', data={'userfile': file}):
        response = subir_imagen()

    # Verificar que se haya devuelto un objeto JSON con los datos esperados
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'doc_type' in json_data
    assert 'confidence' in json_data
    assert 'fields' in json_data
    assert len(json_data['fields']) > 0
