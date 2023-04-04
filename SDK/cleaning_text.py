import re


def analyze_vehiculo_motor(cadena):
    # Expresión regular para buscar las claves de interés
    patron_claves = r'Marca,\s*modelo|Matrícula\s*\(o\s+bastidor\)|País\s+de\s+matrícula'

    # Diccionario para almacenar los resultados  
    dicc = {}

    # Buscar todas las ocurrencias de las claves de interés en el cadena
    claves_encontradas = re.findall(patron_claves, cadena)

    # Iterar sobre las claves encontradas
    for clave_encontrada in claves_encontradas:
        # Expresión regular para buscar la información asociada a la clave
        patron_info = re.escape(clave_encontrada) + r'[\s:]*([\w€, ]+)'
        
        # Buscar la información asociada a la clave
        info_encontrada = re.findall(patron_info, cadena)
        
        # Si se encontró información, agregarla a los resultados
        if info_encontrada:
            resultado =(clave_encontrada.strip() + ' : ' + info_encontrada[0].strip())

        partes = resultado.split(":")
        if len(partes) == 2:
            k, v = partes
            dicc[k.strip()] = v.strip()
    #print(dicc)
    return dicc


analyze_vehiculo_motor('Matrícula (o bastidor)\n63046xw\nMarca, modelo of les end\nPaís de matrícula\n€ Joana')
