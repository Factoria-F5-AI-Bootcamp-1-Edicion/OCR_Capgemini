import json

# Abrir el archivo JSON en modo de lectura
with open('parte_amistoso_0_27.jpg.json', 'r') as archivo:
    # Cargar el contenido del archivo JSON en una variable
    contenido = json.load(archivo)
    datos = contenido["analyzeResult"]["documents"][0]

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

# Crear un diccionario para guardar los diccionarios con los datos
lista_diccionario = {}

for field in datos['fields']:
    campo_buscado = recursive_search(datos, field)      #Recorre lista de campos
    #Imprime contenido del nombre de una etiqueta
    cadena = extraer_content(campo_buscado)
    #print(cadena)
    #print("---------------------------------------------------------------------")

    # Dividir el texto en líneas
    lineas = cadena.split("\n")
    diccionario = {}
    for linea in lineas:
        partes = linea.split(":")
        if len(partes) == 2:
            clave, valor = partes
            diccionario[clave.strip()] = valor.strip()
        elif len(partes) == 3:
            diccionario[partes[0].strip()] = partes[1].strip()

    lista_diccionario[field] = diccionario
    # Escribir la lista de diccionarios en un archivo JSON
    with open("result_test_studio.json", "w") as archivo_json:
        json.dump(lista_diccionario, archivo_json)


    # Mostrar el diccionario resultante
    #print(diccionario)
