import json
import re
from mapping import actualizar_diccionario
from diccionario_plantilla import plantilla, mapeo
from cleaning_text import analyze_vehiculo_motor


def function_load_json(archive_json):
    datos = None
    with open(archive_json, 'r') as archivo:
        # Cargar el contenido del archivo JSON en una variable
        datos = json.load(archivo)
    return datos


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


def guardar_datos(dic_original):
    dic_modificado = {}
    for clave, valor in dic_original.items():
        if isinstance(valor, dict):
            dic_modificado[clave] = guardar_datos(valor)
        elif isinstance(valor, str):
            if clave not in ["Hora", "Fecha", "Lugar", "Testigos", "N°casillas_A", "Nºcasillas_B"]:
                if clave in ['Vehiculo_motor_A', 'Vehiculo_motor_B','Remolque_A', 'Remolque_B']:
                    ## falta mostrar bien Vehiculo a motor y remolque
                    dicc = analyze_vehiculo_motor(valor)
                else:
                    # Definimos la expresión regular que buscará el patrón específico
                    #pattern_remove = re.compile(r"(?<!\s)\n(?!\s)")
                    #valor = re.sub(pattern_remove, "", valor)
                    # Definir patrón
                    # Espacio en blanco delante y despues la exprexion a buscar
                    patron = r'\s+(?=(?:Apell\w+|Direc\w+|C[oó]di\w+|N.º\s\w+|\bPa[ií]s\b(?:[\s:]\w+)?))'
                    dicc = {}
                    # Dividir la cadena según el patrón
                    lineas_patron = re.sub(patron, r'\n\g<0>', valor)
                    lineas = lineas_patron.split("\n")
                    for linea in lineas:
                        partes = linea.split(":")
                        if len(partes) == 2:
                            k, v = partes
                            dicc[k.strip()] = v.strip()
                        elif len(partes) == 3:
                                dicc['Estado'] = partes[1].strip()
                dic_modificado[clave] = dicc
            else:
                dic_modificado[clave] = valor.split('\n')[0]
    #print(dic_modificado)
    return dic_modificado


def function_json_parsing(datos):
    # Abrir el archivo JSON en modo de lectura
    if (datos == None):
        datos = function_load_json("Circ11_B.json")

    # print(datos)
    # Crear un diccionario para guardar los diccionarios con los datos
    lista_diccionario = {}

    lista_diccionario = guardar_datos(datos)

    actualizar_diccionario(plantilla, lista_diccionario, mapeo)

    # print(lista_diccionario)
    # Escribir la lista de diccionarios en un archivo JSON
    with open("result_test_sdk.json", "w") as archivo_json:
        json.dump(plantilla, archivo_json,
                  ensure_ascii=False, sort_keys=True, indent=4)

    return lista_diccionario


function_json_parsing(None)
