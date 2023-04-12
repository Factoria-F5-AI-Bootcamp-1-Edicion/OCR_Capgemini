import re


#Definimos es_clave para saber si contiene un valor o no
def is_info_a_key(info, claves):
    for clave in claves:
          if clave in info:
               return True
    return False


#Definimos funcion para extraer el contenido de tipo string para filtrarlo y limpiarlo por tokens
def analyze_content_text(cadena):
    # Borramos el salto de linea despues de ':'
    patron_remove = r":\n"
    # Reemplazar el patrón por una cadena vacía
    cadena = re.sub(patron_remove, ":", cadena)

    # Definimos la expresión regular que buscará el patrón específico
    # Espacio en blanco delante y despues la exprexion a buscar
    patron = r'\s+(?=(?:Apell\w+|Direc\w+|C[oó]di\w+|Fecha d\w+|N.º\s\w+|\bPa[ií]s\b|Permis\w+(?:[\s:]\w+)?))'

    dicc = {}
    # Dividir la cadena según el patrón
    lineas_patron = re.sub(patron, r'\n\g<0>', cadena)
    lineas = lineas_patron.split("\n")
    for linea in lineas:
        partes = linea.split(":")
        if len(partes) == 2:
            k, v = partes
            dicc[k.strip()] = v.strip().lower()
        elif len(partes) == 3:
                dicc[partes[0].strip()] = partes[1].strip().lower()
    #print(dicc)
    return dicc


#Definimos funcion para extraer el contenido de tipo string para filtrarlo y limpiarlo por tokens en las etiquetas VEHICULO_MOTOR y REMOLQUE
def analyze_vehiculo_motor_and_remolque(cadena):
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
            if is_info_a_key(info_encontrada[0], claves_encontradas):
                 resultado =(clave_encontrada.strip() + ' : ' + '')
            else:
                resultado =(clave_encontrada.strip() + ' : ' + info_encontrada[0].strip())

            partes = resultado.split(":")
            if len(partes) == 2:
                k, v = partes
                dicc[k.strip()] = v.strip().lower()
    #print(dicc)
    return dicc


#analyze_content_text("NOMBRE: Monica Apellidos: Ramos\nDirección: C/ Morales 7 Código Postal: 12211 País: Lituania\nTel. o E-mail: Lazaro.josefa@gmail.com")
#analyze_vehiculo_motor_and_remolque('Matrícula (o bastidor)\n63046xw\nMarca, modelo of les end\nPaís de matrícula\n€ Joana')
