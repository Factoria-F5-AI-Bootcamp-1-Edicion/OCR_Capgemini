<h1 align="center">
  <p align="left">OCR con Azure Form Recognizer</p>
  <img align="center" width="950" height="300" src="">
</h1>

Este proyecto tiene como objetivo implementar una solución de reconocimiento óptico de caracteres (OCR) utilizando Azure Form Recognizer.

#
## Nosotros 🔮
#
Intentamos seguir practicas eticas basandonos en:

- **Responsabilidad:** Este equipo OCR_Capgemini se compromete a utilizar la IA de manera responsable y ética. La empresa ha desarrollado un marco de principios de IA que establece los valores y las prácticas éticas que guían el desarrollo y el uso de la tecnología de la IA.

- **Transparencia:** Este equipo OCR_Capgemini se esfuerza por ser transparente en cuanto a cómo se desarrolla y se utiliza la IA. La empresa ha desarrollado herramientas y procesos para ayudar a los clientes a comprender cómo se utilizan sus datos y cómo se toman las decisiones con la IA.

- **Explicabilidad:** Este equipo OCR_Capgemini se compromete a proporcionar explicaciones claras y comprensibles sobre cómo se toman las decisiones con la IA. La empresa ha desarrollado herramientas y procesos para ayudar a los clientes a entender el proceso de toma de decisiones de la IA.

- **Privacidad y seguridad:** Este equipo OCR_Capgemini se preocupa por la privacidad y la seguridad de los datos de los clientes. La empresa ha desarrollado políticas y prácticas de privacidad y seguridad para garantizar que los datos de los clientes estén protegidos y que se cumplan las normas y regulaciones de privacidad aplicables.

- **Diversidad e inclusión:** Este equipo OCR_Capgemini se esfuerza por garantizar que la IA sea justa e inclusiva. La empresa ha desarrollado herramientas y procesos para ayudar a identificar y mitigar los sesgos en los sistemas de IA y para garantizar que la tecnología sea accesible para todos.

#
## Aplicación de partes de seguros de automóviles  💻 
#

<h1 align="center">
  <img align="center" width="950" height="450" src="https://user-images.githubusercontent.com/74676901/227197818-e0221aa9-42bf-4722-864f-e0c1e3934717.png">
</h1>

Esta aplicación tiene como objetivo simplificar y mejorar el proceso de gestión de partes de seguros de automóviles con el recurso de Microsoft Azure Form Recognizer para que tenga capacidades de reconocimiento de texto e identificación de entidades.

 - Tenemos un conjunto de datos con partes amistosos de accidentes automovilisticos.
 - Estos archivos se subiran a un contenedor en una cuenta de almacenamiento de Azure (si no se encuentra creada, se debe crear).
 - Se crea el recurso Form Recognizer studio y se vincula al contenedor donde se guardaran los datos.
 - Se entrenará y creará un primer modelo de reconocimiento a partir de cinco imagenes (Form Recognizer Studio o con SDK de Python).
 - Y por ultimo de analiza el modelo entrenado con una imagen que no se encuentre en el contenedor.

#
## Variables de Entorno requeridas
Se debe crear un archivo `.env`, donde se configuren las variables de entorno necesarias y requeridas para la conexión segura a la base de datos y asegurar la externalización de datos sensibles.

| Variable de entorno                | Descripción                          | Ejemplo                |
|------------------------------------|--------------------------------------|------------------------|
| `AZURE_FORM_RECOGNIZER_ENDPOINT`   | Endpoint del recurso de Recognizer   | `postgres`             |
| `AZURE_FORM_RECOGNIZER_KEY`        | Key del recurso de Recognizer        | `postgres`             |
| `CONTAINER_SAS_URL`                | SAS URL del contenedor               | `localhost`            |
| `AZURE_STORAGE_CONNECTION_STRING`  | Cadena de conexion del contenedor    | `5432`                 |

#
### Tecnologías utilizadas 🛠️

Esta aplicación ha sido desarrollada utilizando las siguientes tecnologías:

- **Desarrollo:**
    - SDK de Python
    - Azure Form Recognizer
    - Json
    - Python
- **Presentación:**
    - Canva.

#
### Instalación 🤖


1.  Clona este repositorio en tu máquina local.
2.  Ejecuta `npm install` para instalar todas las dependencias necesarias.
3.  Ejecuta `npm start` para iniciar la aplicación.

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
#
Este proyecto ha sido desarrollado por los siguientes participantes:

- Andrea Sandoval  👩‍💻
- Anghi Sanchez  👩‍💻
- Raúl 👨‍💻
- Víctor Arbiol👨‍💻

#
## Licencia
#

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más información.
