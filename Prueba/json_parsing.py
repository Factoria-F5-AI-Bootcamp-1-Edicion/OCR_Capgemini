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
    return campo_buscado['content']


campo_buscado = recursive_search(datos, "ConductorA")
imprime_contenido = extraer_content(campo_buscado)


print(imprime_contenido)