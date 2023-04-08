import json
import re
from mapping import actualizar_diccionario, update_keys
from diccionario_plantilla import plantilla, plantilla2, mapeo, mapeo2
from cleaning_text import analyze_content_text, analyze_vehiculo_motor_and_remolque


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
                    dicc = analyze_vehiculo_motor_and_remolque(valor)
                else:
                    dicc = analyze_content_text(valor)
                dic_modificado[clave] = dicc
            else:
                dic_modificado[clave] = valor.split('\n')[0].lower()
    #print(dic_modificado)
    return dic_modificado


def function_json_parsing(datos):
    # Abrir el archivo JSON en modo de lectura
    if (datos == None):
        datos = function_load_json("Circ11_B.json")

    # print(datos)
    # Crear un diccionario para guardar los diccionarios con los datos
    lista_diccionario = {}
    data = {}

    diccionario_final = plantilla
    # Filtramos y limpiamos los datos json entregados
    lista_diccionario = guardar_datos(datos)
    # Actualizamos el json filtrado y limpio a la nueva plantilla para que se visualice de manera bonita
    #print(lista_diccionario)
    actualizar_diccionario(diccionario_final, lista_diccionario, mapeo)
    #print(diccionario_final)
    diccionario_final = update_keys(diccionario_final)
    #print(diccionario_final)


    '''
    for k, v in datos.items():

        # Dividir el texto en líneas
        #print(k)
        #print(v)
        diccionario = {}
        if '\n' not in v:
            lista_diccionario[k]=v

        else:
            # Definir patrón
            patron = r'\s+(?=(?:Apell\w+|Direc\w+|C[oó]di\w+|N.º\s\w+|\bPa[ií]s\b(?:[\s:]\w+)?|Fecha\s\w+))'  # Espacio en blanco delante y despues la exprexion a buscar

            # Dividir la cadena según el patrón
            lineas_patron = re.sub(patron, r'\n\g<0>', v)
            lineas = lineas_patron.split("\n")
            #print(lineas)
            for linea in lineas:
                partes = linea.split(":")
                if len(partes) == 2:
                    clave, valor = partes
                    diccionario[clave.strip()] = valor.strip()
                elif len(partes) == 3:
                    diccionario[partes[0].strip()] = partes[1].strip()

        lista_diccionario[k] = diccionario
    '''

    # Guardamos nuestra plantilla presentable y con los datos ya limpios en un archivo JSON
    with open("result_test_sdk.json", "w") as archivo_json:
        json.dump(diccionario_final, archivo_json,
                  ensure_ascii=False, sort_keys=True, indent=4)

    return diccionario_final

function_json_parsing(None)

