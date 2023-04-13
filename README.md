
<h1 align=center> Reconocimiento Óptico de Caracteres con Form Recognizer de Azure </h1>
 <img src="https://user-images.githubusercontent.com/108665291/229485641-469dbf9a-99f3-4a23-b34d-306007968ab9.jpg" width="1000px" align=lesft>

El objetivo principal del proyecto es crear una solución tecnológica que permita a la empresa SEGUROS SL optimizar la entrada y distribución de documentación, mediante el desarrollo de capacidades de reconocimiento de texto, con el fin de automatizar la extracción de información y los procesos asociados a ella. El proyecto busca mejorar la gestión de documentos y la transformación digital de la organización, centrando la actividad en el cliente y utilizando la inteligencia artificial para extraer información de los documentos de manera automatizada.

#
## Nosotros 🔮
<img src="https://user-images.githubusercontent.com/108665291/229771836-a117e07f-50d6-485a-8413-c39ac50fd341.png" width="400px" align=right>

Somos un grupo de estudiantes de Factoría F5 y estamos emocionados de presentar nuestro proyecto final pedagógico para la empresa líder en consultoría y servicios tecnológicos, Capgemini.
Nuestro proyecto final, utiliza nuestra experiencia en IA y aprendizaje automático para abordar un problema empresarial clave de Seguros SL. Nuestra solución es innovadora, eficiente y diseñada específicamente para satisfacer las necesidades de la empresa.



Intentamos seguir practicas eticas basandonos en:

- **Responsabilidad:** Este equipo se compromete a utilizar la IA de manera responsable y ética. Hemos desarrollado un marco de principios de IA que establece los valores y las prácticas éticas que guían el desarrollo y el uso de la tecnología de la IA.

- **Transparencia:** Este equipo se esfuerza por ser transparente en cuanto a cómo se desarrolla y se utiliza la IA. La empresa ha desarrollado herramientas y procesos para ayudar a los clientes a comprender cómo se utilizan sus datos y cómo se toman las decisiones con la IA.

- **Explicabilidad:** Este equipo se compromete a proporcionar explicaciones claras y comprensibles sobre cómo se toman las decisiones con la IA. La empresa ha desarrollado herramientas y procesos para ayudar a los clientes a entender el proceso de toma de decisiones de la IA.

- **Privacidad y seguridad:** Este equipo se preocupa por la privacidad y la seguridad de los datos de los clientes. La empresa ha desarrollado políticas y prácticas de privacidad y seguridad para garantizar que los datos de los clientes estén protegidos y que se cumplan las normas y regulaciones de privacidad aplicables.

- **Diversidad e inclusión:** Este equipo se esfuerza por garantizar que la IA sea justa e inclusiva. La empresa ha desarrollado herramientas y procesos para ayudar a identificar y mitigar los sesgos en los sistemas de IA y para garantizar que la tecnología sea accesible para todos.

#
## Aplicación de partes de seguros de automóviles  💻 



<h1 align="center">
  <img align="center" width="950" height="500" src="https://user-images.githubusercontent.com/74676901/227197818-e0221aa9-42bf-4722-864f-e0c1e3934717.png">
</h1>

Esta aplicación tiene como objetivo simplificar y mejorar el proceso de gestión de partes de seguros de automóviles con el recurso de Microsoft Azure Form Recognizer para que tenga capacidades de reconocimiento de texto e identificación de entidades.

 - Tenemos un conjunto de datos con partes amistosos de accidentes automovilisticos.
 - Estos archivos se subiran a un contenedor en una cuenta de almacenamiento de Azure (si no se encuentra creada, se debe crear).
 - Se crea el recurso Form Recognizer studio y se vincula al contenedor donde se guardaran los datos.
 - Se entrenará y creará un primer modelo de reconocimiento a partir de cinco imagenes (Form Recognizer Studio o con SDK de Python).
 - Y por ultimo se analiza el modelo entrenado con una imagen que no se encuentre en el contenedor.
 - El resultado del análisis con el OCR , debe devolver un archico en formato Json con al información solicitada.
#
## Acceso al proyecto 📁

*Descarga el contenido del repositorio* >>  https://github.com/Factoria-F5-AI-Bootcamp-1-Edicion/OCR_Capgemini.git

## 🛠️ Abre y ejecuta el proyecto

1. Crea un entorno específicamente para este proyecto. Por ejemplo con conda 
```
conda create -n nombreEntorno
```
2. Dentro de este entorno será necesario instalar todas las librerias usadas, lo puedes hacer desde archivo :
```
requirements.txt
```
3. Crear una carpeta llamada *Images* en la misma ruta en la que se encuentra el servidor de la API
```
mkdir <ruta-de-la-carpeta>
```
4. Crear 2 archivos .env para almacenar las variables de entorno de la conexión con Form Recognizer, tanto en la ruta de la API como en la de SDK
```
touch .env 

```
5. Desde la terminal, situate en la carpeta que contiene los archivos de la API y desde allí ejecute
```
flask run 
```
6. Esto nos llevará al servidor de la API , donde podremos subir el documento que queremos analizar y nos permitirá descargar el json que se genera.

<h1 align="center">
  <img align="center" width="400" height="200" src="https://user-images.githubusercontent.com/74676901/230013367-5f26ddc5-fea0-4d5a-82ba-468af0912d92.png">

</h1>

## Testing de la API 🤖 
1. Para poder realizar el test debemos subir una imagen en la ruta donde se encuentra el archivo de testeo
```
ejemplo : parte_test.jpg
```

2. Para probar el test de la API, ejecurte:
```
pytest test_app.py
```


#
## Variables de Entorno requeridas
Se debe crear un archivo `.env`, donde se configuren las variables de entorno necesarias y requeridas para la conexión segura a la base de datos y asegurar la externalización de datos sensibles.

| Variable de entorno                | Descripción                          | 
|------------------------------------|--------------------------------------|
| `AZURE_FORM_RECOGNIZER_ENDPOINT`   | Endpoint del recurso de Recognizer   |
| `AZURE_FORM_RECOGNIZER_KEY`        | Key del recurso de Recognizer        | 
| `CONTAINER_SAS_URL`                | SAS URL del contenedor               | 
| `AZURE_STORAGE_CONNECTION_STRING`  | Cadena de conexion del contenedor    | 


#
## Acceso a la aplicación con docker 📁
### Docker facilita su despliegue y escalabilidad. 

El proceso de despliegue se puede usar junto con CD/CI, se puede usar con github jenkinns detectará 
si hay algún cambio en la rama Main, disparando un script bash que genera la descarga del repositorio, 
la creación del docker, su posterior subida a hub-docker conectada a azure, instances container.

**Descarga el contenido de docker hub** 

docker push systemdeveloper868/capgemini

**Para lanzar la aplicacion en local:**

docker run -d -p 8000:8000 systemdeveloper868/capgemini 

**Para entrar en la aplicación por el navegador**

http://20.8.201.32:8000/


#
### Tecnologías utilizadas 🛠️

Esta aplicación ha sido desarrollada utilizando las siguientes tecnologías:

- **Desarrollo:**
    - SDK de cliente
    - Form Recognizer Studio
    - Json
    - Jsonlint
    - Dotenv
    - Python
 - **API:**
    - Flask
    - Pytest
    - Unitest
- **Front:**
    - HTML
    - CSS
    - Bootstrap
- **Metodología SCRUM:**
    - [Trello](https://trello.com/invite/b/Rz1msFgX/ATTIf42a43f957186c8e6f6e2e59856bbb911DAD7F45/capgemini-ocr) 
- **Presentación:**
    - [Canva](https://www.canva.com/design/DAFfufaJU2M/tCnzZKI7jdO_yXRh2_rQCA/edit)
- **Documentación:**
    - [Notion](https://carpal-pyramid-f1c.notion.site/Form-Recognizer-de-Azure-)

#
### Contribuciones 📁


Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1.  Haz un fork de este repositorio.
2.  Crea una nueva rama con tu contribución: `git checkout -b mi_contribucion`.
3.  Haz tus cambios y realiza un commit: `git commit -m "Mi contribución"`.
4.  Realiza un push a la rama: `git push origin mi_contribucion`.
5.  Crea un pull request y describe tus cambios.

#
## Participantes

Este proyecto ha sido desarrollado por los siguientes participantes:

- Andrea Sandoval  👩‍💻
- Anghi Sanchez  👩‍💻
- Raúl Muñoz 👨‍💻
- Víctor Arbiol 👨‍💻

<p align=center><em> Transforma la gestión de partes de seguros de automóviles con la inteligencia de Microsoft Azure Form Recognizer </em></p>


