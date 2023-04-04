import json
import re
from Prueba.mapping import actualizar_diccionario
from diccionario_plantilla import plantilla, mapeo

def function_load_json(archive_json):
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
            if '\n' in valor and clave not in ["Hora", "Fecha", "Lugar", "Testigos", "Vehiculo_motor_A", "Vehiculo_motor_B", "Remolque_A", "Remolque_B"]:
                # Definimos la expresión regular que buscará el patrón específico
                #pattern_remove = re.compile(r"(?<!\s)\n(?!\s)")
                #valor = re.sub(pattern_remove, "", valor)
                # Definir patrón
                patron = r'\s+(?=(?:Apell\w+|Direc\w+|C[oó]di\w+|N.º\s\w+|\bPa[ií]s\b(?:[\s:]\w+)?))'  # Espacio en blanco delante y despues la exprexion a buscar
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
                        dicc[partes[0].strip()] = partes[1].strip()
                dic_modificado[clave] = dicc
            else:
                if clave not in ["VehiculoA", "VehiculoB"]:
                    dic_modificado[clave] = valor.split('\n')[0]
                else:
                    dic_modificado[clave] = valor
    return dic_modificado

def function_json_parsing(datos):
    # Abrir el archivo JSON en modo de lectura
    if (datos == None):
        function_load_json("result_1_test.json")

    # Crear un diccionario para guardar los diccionarios con los datos
    lista_diccionario = {}
    data = {}

    lista_diccionario = guardar_datos(datos)

    #actualizar_diccionario(plantilla, lista_diccionario, mapeo)

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
    data= lista_diccionario
    # Escribir la lista de diccionarios en un archivo JSON
    with open("result_test_sdk_2.json", "w") as archivo_json:
            json.dump(lista_diccionario, archivo_json, ensure_ascii=False, sort_keys=True, indent=4 )

    return data