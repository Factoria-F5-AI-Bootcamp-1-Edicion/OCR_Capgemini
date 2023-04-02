import json
import re


def function_load_json(archive_json):
    with open(archive_json, 'r') as archivo:
        # Cargar el contenido del archivo JSON en una variable
        datos = json.load(archivo)


def recursive_search(d, k):
    if k in d:
        return d[k]
    for v in d.values():
        if isinstance(v, dict):
            x = recursive_search(v, k)
            if x is not None:
                return x


def extraer_content(campo_buscado):
    if campo_buscado.get("content") is not None:
        return campo_buscado['content']
    else:
        return ""


def function_json_parsing(datos):
    # Abrir el archivo JSON en modo de lectura
    if (datos == None):
        function_load_json("result_1_test.json")

    # Crear un diccionario para guardar los diccionarios con los datos
    lista_diccionario = {}
    data = {}

    for k, v in datos.items():

        # Dividir el texto en líneas

        diccionario = {}

        # Definir patrón
        patron = r'\s+(?=(?:Apell\w+|Direc\w+|C[oó]di\w+|N.º\s\w+|\bPa[ií]s\b(?:[\s:]\w+)?|Fecha\s\w+))'  # Espacio en blanco delante y despues la exprexion a buscar

        # Dividir la cadena según el patrón
        lineas_patron = re.sub(patron, r'\n\g<0>', v)
        lineas = lineas_patron.split("\n")
        print(lineas)
        for linea in lineas:
            partes = linea.split(":")
            if len(partes) == 2:
                clave, valor = partes
                diccionario[clave.strip()] = valor.strip()
            elif len(partes) == 3:
                diccionario[partes[0].strip()] = partes[1].strip()

        lista_diccionario[k] = diccionario
        data= lista_diccionario
        # Escribir la lista de diccionarios en un archivo JSON
        with open("result_test_sdk_2.json", "w") as archivo_json:
            json.dump(lista_diccionario, archivo_json, ensure_ascii=False, sort_keys=True, indent=4 )

    return data