import json
from diccionario_plantilla import plantilla, plantilla2, mapeo, mapeo2
'''
plantilla = {
    "Fecha": {},
    "Hora": {},
    "Lugar": {},
    "Testigos": {},
    "VehiculoA": {
        "AseguradoA": {"NOMBRE": "Monica", "Apellidos": "Ramos", "Direcci\u00f3n": "C/ Morales 7", "C\u00f3digo Postal": "12211", "Pa\u00eds": "Lituania", "Tel. o E-mail": "Lazaro.josefa@gmail.com"}, 
        "AseguradoraA": {"NOMBRE": "Essalud", "N.\u00ba de p\u00f3liza": "2.3.63", "N.\u00ba de Carta Verde": "1455", "Certificado": "o Carta Verde v\u00e1lida desde 2/8 hasta 1/39", "Agencia (oficina o corredor)": "Rs rove", "Nombre": "Gabriel", "Direcci\u00f3n": "C/ rico 57", "Pa\u00eds": "EJoana", "Tel. o E-mail": "Ortiz.enrique@gmail.es"},
        "ConductorA": {"NOMBRE": "Rosario", "Apellidos": "Ruiz", "Fecha de nacimiento": "25/6/1971", "Direcci\u00f3n": "Calle Lara 97", "Pa\u00eds": "Espana", "Tel. o E-mail": "", "Permiso de conducir n.\u00ba": "127949371", "Categoría": "", "Permiso v\u00e1lido hasta": "21/6/2039"}, 
        
        "Circ1": {"Concepto":"Está estacionado/parado", "Estado":"unselected"},
        "Circ2": {"Concepto":"Salia de un estacionamiento/abriendo puerta", "Estado":"unselected"},
        "Circ3": {"Concepto":"Iba a estacionar", "Estado":"unselected"},
        "Circ4": {"Concepto":"Salía de un aparcamiento, de un lugar privado o un camino de tierra", "Estado":"unselected"},
        "Circ5": {"Concepto":"Entrada a un aparcamiento, de un lugar privado o un camino de tierra", "Estado":"unselected"},
        "Circ6": {"Concepto":"Entrada a una plaza de sentido giratorio", "Estado":"unselected"},
        "Circ7": {"Concepto":"Circulaba a una plaza de sentido giratorio", "Estado":"unselected"},
        "Circ8": {"Concepto":"Colisiono en la parte de atras al otro vehiculo que circulaba en el mismo sentido y en el mismo carril", "Estado":"unselected"},
        "Circ9": {"Concepto":"Circulaba en el mismo sentido y distinto carril", "Estado":"unselected"},
        "Circ10": {"Concepto":"Cambiaba de carril", "Estado":"unselected"},
        "Circ11": {"Concepto":"Adelantaba", "Estado":"unselected"},
        "Circ12": {"Concepto":"Giraba a la derecha", "Estado":"unselected"},
        "Circ13": {"Concepto":"Daba marcha atras", "Estado":"unselected"},
        "Circ15": {"Concepto":"Invadia la parte reservada a la circulacion en sentido inverso", "Estado":"unselected"},
        "Circ16": {"Concepto":"Venia de la derecha(en un cruce)", "Estado":"unselected"},
        "Circ17": {"Concepto":"No respeto la señal de preferencia o semaforo en rojo", "Estado":"unselected"},       
        "N\u00b0casillas_A": {"Estado": "unselected"}, 
    },
    "VehiculoB": {   
        "AseguradoB": {"NOMBRE": "Alfredo", "Apellidos": "Rodriguez", "Direcci\u00f3n": "C/ vera 13", "C\u00f3digo Postal": "13242", "Pa\u00eds": "Lituania", "Tel. o E-mail": ""}, 
        "AseguradoraB": {"NOMBRE": "Catalana occidente", "N.\u00ba de p\u00f3liza": "2373", "N.\u00ba de Carta Verde": "62413", "Certificado": "", "Agencia (oficina o corredor)": "Menasalbas", "Nombre": "Lusa", "Direcci\u00f3n": "01 ruiz 16", "Pa\u00eds": "SJoana"}, 
        "ConductorB": {"NOMBRE": "Juan Luis", "Apellidos": "Salas", "Fecha de nacimiento": "9/2/1936", "Direcci\u00f3n": "01 camp os 12", "Pa\u00eds": "Espa\u00f1a", "Tel. o E-mail": "", "Permiso de conducir n.\u00ba": "786181234", "Categoría": "", "Permiso v\u00e1lido hasta": "27/6/2025"}, 
        
        "Circ1": {"Concepto":"Está estacionado/parado", "Estado":"unselected"},
        "Circ2": {"Concepto":"Salia de un estacionamiento/abriendo puerta", "Estado":"unselected"},
        "Circ3": {"Concepto":"Iba a estacionar", "Estado":"unselected"},
        "Circ4": {"Concepto":"Salía de un aparcamiento, de un lugar privado o un camino de tierra", "Estado":"unselected"},
        "Circ5": {"Concepto":"Entrada a un aparcamiento, de un lugar privado o un camino de tierra", "Estado":"unselected"},
        "Circ6": {"Concepto":"Entrada a una plaza de sentido giratorio", "Estado":"unselected"},
        "Circ7": {"Concepto":"Circulaba a una plaza de sentido giratorio", "Estado":"unselected"},
        "Circ8": {"Concepto":"Colisiono en la parte de atras al otro vehiculo que circulaba en el mismo sentido y en el mismo carril", "Estado":"unselected"},
        "Circ9": {"Concepto":"Circulaba en el mismo sentido y distinto carril", "Estado":"unselected"},
        "Circ10": {"Concepto":"Cambiaba de carril", "Estado":"unselected"},
        "Circ11": {"Concepto":"Adelantaba", "Estado":"unselected"},
        "Circ12": {"Concepto":"Giraba a la derecha", "Estado":"unselected"},
        "Circ13": {"Concepto":"Daba marcha atras", "Estado":"unselected"},
        "Circ15": {"Concepto":"Invadia la parte reservada a la circulacion en sentido inverso", "Estado":"unselected"},
        "Circ16": {"Concepto":"Venia de la derecha(en un cruce)", "Estado":"unselected"},
        "Circ17": {"Concepto":"No respeto la señal de preferencia o semaforo en rojo", "Estado":"unselected"},

        "N\u00b0casillas_B": {"Estado": "unselected"},
    }
}
'''

def modificar_diccionario(diccionario_original, diccionario_a_modificar):
    for clave, valor in diccionario_original.items():
        if isinstance(valor, dict) and clave in diccionario_a_modificar.items():
            print(clave)
            modificar_diccionario(valor, diccionario_a_modificar[clave])
        elif clave in diccionario_a_modificar:
            if clave == "":
                clave = "Estado"
                diccionario_a_modificar[clave] = valor
    
    with open('test_result.json', 'w') as f:
        json.dump(diccionario_a_modificar, f)


def recorrer_diccionario(diccionario):
    """
    Recorre de manera recursiva el diccionario si encuentra la clave y modifica su valor.
    """
    diccionario_result={}
    # Creamos una copia de la plantilla
    #planti = function_load_json("plantilla.json")
    diccionario_modificado = plantilla.copy()
    for clave, valor in diccionario.items():
        if isinstance(valor, dict):
            recorrer_diccionario(valor)
        else:
            # hacer algo con la clave y el valor aquí
            #print(clave, valor)
            # Si la clave existe en el diccionario a modificar, asignamos el valor correspondiente
            diccionario_modificado= modificar_valor(diccionario_modificado, clave, diccionario[clave])
                #print(clave)

    # Imprimimos el diccionario modificado
    #print(diccionario_modificado)


# Función para actualizar el diccionario_plantilla
def actualizar_diccionario(diccionario_plantilla, diccionario_original, mapeo):
    for clave, valor in diccionario_plantilla.items():
        if isinstance(valor, dict) and clave not in ['Vehiculo_motor_A', 'Vehiculo_motor_B']:
            if isinstance(mapeo[clave], dict):
                #print(mapeo[clave])
                actualizar_diccionario(valor, diccionario_original[clave], mapeo[clave])
            else:
                actualizar_diccionario(valor, diccionario_original[mapeo[clave]], mapeo)
        else:
            #print(mapeo)
            #print(bool(mapeo[clave] in diccionario_original))
            if clave in ['Vehiculo_motor_A', 'Vehiculo_motor_B']:
                diccionario_plantilla[clave] = diccionario_original[clave]
            elif mapeo[clave] in diccionario_original:
                diccionario_plantilla[clave] = diccionario_original[mapeo[clave]]
            else:
                diccionario_plantilla[clave] = valor

# función recursiva para actualizar las claves del diccionario anidado
def update_keys(d, parent_key=None):
    if isinstance(d, dict):
        new_dict = {}
        for k, v in d.items():
            new_key = mapeo2.get(k, k)
            if isinstance(v, dict):
                v = update_keys(v, parent_key=new_key)
            if new_key in new_dict:
                #print(new_dict)
                #print(v)
                new_dict[new_key].update(v)
            else:
                new_dict[new_key] = v
        return new_dict
    else:
        return d

# Función para actualizar el diccionario_plantilla
def modificacion_plantilla2(plantilla2, datos):
        # Metemos directamente una a una: la clave en cada diccionario es distinta y los niveles de arbol de diccionario
        plantilla2["FECHA"] = datos["Fecha"]
        plantilla2["HORA"] = datos["Hora"]
        plantilla2["LUGAR"] = datos["Lugar"]
        plantilla2["TESTIGOS"] = datos["Testigos"]

        print(datos["AseguradoA"])['NOMBRE']

        plantilla2["VEHICULO_A"]["ASEGURADO_A"]["NOMBRE"] = datos["AseguradoA"]["NOMBRE"]
        plantilla2["VEHICULO_A"]["ASEGURADO_A"]["APELLIDOS"] = datos["AseguradoA"]["Apellidos"]
        plantilla2["VEHICULO_A"]["ASEGURADO_A"]["DIRECCION"] = datos["AseguradoA"]["Direcci\u00f3n"]
        plantilla2["VEHICULO_A"]["ASEGURADO_A"]["CODIGO_POSTAL"] = datos["AseguradoA"]["C\u00f3digo Postal"]
        plantilla2["VEHICULO_A"]["ASEGURADO_A"]["PAIS"] = datos["AseguradoA"]["Pa\u00eds"]
        plantilla2["VEHICULO_A"]["ASEGURADO_A"]["TEL. O E-MAIL"] = datos["AseguradoA"]["Tel. o E-mail"]
        
        plantilla2["VEHICULO_A"]["ASEGURADORA_A"]["NOMBRE"] = datos["AseguradoraA"]["NOMBRE"]
        plantilla2["VEHICULO_A"]["ASEGURADORA_A"]["Nº DE POLIZA"] = datos["AseguradoraA"]["N.\u00ba de p\u00f3liza"]
        plantilla2["VEHICULO_A"]["ASEGURADORA_A"]["N.º DE CARTA VERDE"] = datos["AseguradoraA"]["N.\u00ba de Carta Verde"]
        plantilla2["VEHICULO_A"]["ASEGURADORA_A"]["CERTIFICADO"] = datos["AseguradoraA"]["Certificado"]
        plantilla2["VEHICULO_A"]["ASEGURADORA_A"]["AGENCIA (OFICINA O CORREDOR)"] = datos["AseguradoraA"]["Agencia (oficina o corredor)"]
        plantilla2["VEHICULO_A"]["ASEGURADORA_A"]["NOMBRE_AGENCIA"] = datos["AseguradoraA"]["Nombre"]
        plantilla2["VEHICULO_A"]["ASEGURADORA_A"]["DIRECCION_AGENCIA"] = datos["AseguradoraA"]["Direcci\u00f3n"]
        plantilla2["VEHICULO_A"]["ASEGURADORA_A"]["PAIS_AGENCIA"] = datos["AseguradoraA"]["Pa\u00eds"]

        plantilla2["VEHICULO_A"]["CONDUCTOR_A"]["NOMBRE"] = datos["ConductorA"]["NOMBRE"]
        plantilla2["VEHICULO_A"]["CONDUCTOR_A"]["APELLIDOS"] = datos["ConductorA"]["Apellidos"]
        plantilla2["VEHICULO_A"]["CONDUCTOR_A"]["FECHA DE NACIMIENTO"] = datos["ConductorA"]["Fecha de nacimiento"]
        plantilla2["VEHICULO_A"]["CONDUCTOR_A"]["DIRECCION"] = datos["ConductorA"]["Direcci\u00f3n"]
        plantilla2["VEHICULO_A"]["CONDUCTOR_A"]["PAIS"] = datos["ConductorA"]["Pa\u00eds"]
        plantilla2["VEHICULO_A"]["CONDUCTOR_A"]["TEL. o E-MAIL"] = datos["ConductorA"]["Tel. o E-mail"]
        plantilla2["VEHICULO_A"]["CONDUCTOR_A"]["PERMISO DE CONDUCIR n.\u00ba"] = datos["ConductorA"]["Permiso de conducir n.\u00ba"]
        plantilla2["VEHICULO_A"]["CONDUCTOR_A"]["CATEGORIA(A,B,...)"] = datos["ConductorA"]["Categoría"]
        plantilla2["VEHICULO_A"]["CONDUCTOR_A"]["PERMISO VALIDO HASTA"] = datos["ConductorA"]["Permiso v\u00e1lido hasta"]

        plantilla2["VEHICULO_A"]["CIRC1"]["ESTADO"] = datos["Circ1_A"][1]
        plantilla2["VEHICULO_A"]["CIRC2"]["ESTADO"] = datos["Circ2_A"][1]
        plantilla2["VEHICULO_A"]["CIRC3"]["ESTADO"] = datos["Circ3_A"][1]
        plantilla2["VEHICULO_A"]["CIRC4"]["ESTADO"] = datos["Circ4_A"][1]
        plantilla2["VEHICULO_A"]["CIRC5"]["ESTADO"] = datos["Circ5_A"][1]
        plantilla2["VEHICULO_A"]["CIRC6"]["ESTADO"] = datos["Circ6_A"][1]
        plantilla2["VEHICULO_A"]["CIRC7"]["ESTADO"] = datos["Circ7_A"][1]
        plantilla2["VEHICULO_A"]["CIRC8"]["ESTADO"] = datos["Circ8_A"][1]
        plantilla2["VEHICULO_A"]["CIRC9"]["ESTADO"] = datos["Circ9_A"][1]
        plantilla2["VEHICULO_A"]["CIRC10"]["ESTADO"] = datos["Circ10_A"][1]
        plantilla2["VEHICULO_A"]["CIRC11"]["ESTADO"] = datos["Circ11_A"][1]
        plantilla2["VEHICULO_A"]["CIRC12"]["ESTADO"] = datos["Circ12_A"][1]
        plantilla2["VEHICULO_A"]["CIRC13"]["ESTADO"] = datos["Circ13_A"][1]
        plantilla2["VEHICULO_A"]["CIRC14"]["ESTADO"] = datos["Circ14_A"][1]
        plantilla2["VEHICULO_A"]["CIRC15"]["ESTADO"] = datos["Circ15_A"][1]
        plantilla2["VEHICULO_A"]["CIRC16"]["ESTADO"] = datos["Circ16_A"][1]
        plantilla2["VEHICULO_A"]["CIRC17"]["ESTADO"] = datos["Circ17_A"][1]

        plantilla2["VEHICULO_B"]["ASEGURADO_B"]["NOMBRE"] = datos["AseguradoB"]["NOMBRE"]
        plantilla2["VEHICULO_B"]["ASEGURADO_B"]["APELLIDOS"] = datos["AseguradoB"]["Apellidos"]
        plantilla2["VEHICULO_B"]["ASEGURADO_B"]["DIRECCION"] = datos["AseguradoB"]["Direcci\u00f3n"]
        plantilla2["VEHICULO_B"]["ASEGURADO_B"]["CODIGO_POSTAL"] = datos["AseguradoB"]["C\u00f3digo Postal"]
        plantilla2["VEHICULO_B"]["ASEGURADO_B"]["PAIS"] = datos["AseguradoB"]["Pa\u00eds"]
        plantilla2["VEHICULO_B"]["ASEGURADO_B"]["TEL. O E-MAIL"] = datos["AseguradoB"]["Tel. o E-mail"]
        
        plantilla2["VEHICULO_B"]["ASEGURADORA_B"]["NOMBRE"] = datos["AseguradoraB"]["NOMBRE"]
        plantilla2["VEHICULO_B"]["ASEGURADORA_B"]["Nº DE POLIZA"] = datos["AseguradoraB"]["N.\u00ba de p\u00f3liza"]
        plantilla2["VEHICULO_B"]["ASEGURADORA_B"]["N.º DE CARTA VERDE"] = datos["AseguradoraB"]["N.\u00ba de Carta Verde"]
        plantilla2["VEHICULO_B"]["ASEGURADORA_B"]["CERTIFICADO"] = datos["AseguradoraB"]["Certificado"]
        plantilla2["VEHICULO_B"]["ASEGURADORA_B"]["AGENCIA (OFICINA O CORREDOR)"] = datos["AseguradoraB"]["Agencia (oficina o corredor)"]
        plantilla2["VEHICULO_B"]["ASEGURADORA_B"]["NOMBRE_AGENCIA"] = datos["AseguradoraB"]["Nombre"]
        plantilla2["VEHICULO_B"]["ASEGURADORA_B"]["DIRECCION_AGENCIA"] = datos["AseguradoraB"]["Direcci\u00f3n"]
        plantilla2["VEHICULO_B"]["ASEGURADORA_B"]["PAIS_AGENCIA"] = datos["AseguradoraB"]["Pa\u00eds"]

        plantilla2["VEHICULO_B"]["CONDUCTOR_B"]["NOMBRE"] = datos["ConductorB"]["NOMBRE"]
        plantilla2["VEHICULO_B"]["CONDUCTOR_B"]["APELLIDOS"] = datos["ConductorB"]["Apellidos"]
        plantilla2["VEHICULO_B"]["CONDUCTOR_B"]["FECHA DE NACIMIENTO"] = datos["ConductorB"]["Fecha de nacimiento"]
        plantilla2["VEHICULO_B"]["CONDUCTOR_B"]["DIRECCION"] = datos["ConductorB"]["Direcci\u00f3n"]
        plantilla2["VEHICULO_B"]["CONDUCTOR_B"]["PAIS"] = datos["ConductorB"]["Pa\u00eds"]
        plantilla2["VEHICULO_B"]["CONDUCTOR_B"]["TEL. o E-MAIL"] = datos["ConductorB"]["Tel. o E-mail"]
        plantilla2["VEHICULO_B"]["CONDUCTOR_B"]["PERMISO DE CONDUCIR n.\u00ba"] = datos["ConductorB"]["Permiso de conducir n.\u00ba"]
        plantilla2["VEHICULO_B"]["CONDUCTOR_B"]["CATEGORIA(A,B,...)"] = datos["ConductorB"][")"]
        plantilla2["VEHICULO_B"]["CONDUCTOR_B"]["PERMISO VALIDO HASTA"] = datos["ConductorB"]["Permiso v\u00e1lido hasta"]

        plantilla2["VEHICULO_B"]["CIRC1"]["ESTADO"] = datos["Circ1_B"][""]
        plantilla2["VEHICULO_B"]["CIRC2"]["ESTADO"] = datos["Circ2_B"][""]
        plantilla2["VEHICULO_B"]["CIRC3"]["ESTADO"] = datos["Circ3_B"][""]
        plantilla2["VEHICULO_B"]["CIRC4"]["ESTADO"] = datos["Circ4_B"][""]
        plantilla2["VEHICULO_B"]["CIRC5"]["ESTADO"] = datos["Circ5_B"][""]
        plantilla2["VEHICULO_B"]["CIRC6"]["ESTADO"] = datos["Circ6_B"][""]
        plantilla2["VEHICULO_B"]["CIRC7"]["ESTADO"] = datos["Circ7_B"][""]
        plantilla2["VEHICULO_B"]["CIRC8"]["ESTADO"] = datos["Circ8_B"][""]
        plantilla2["VEHICULO_B"]["CIRC9"]["ESTADO"] = datos["Circ9_B"][""]
        plantilla2["VEHICULO_B"]["CIRC10"]["ESTADO"] = datos["Circ10_B"][""]
        plantilla2["VEHICULO_B"]["CIRC11"]["ESTADO"] = datos["Circ11_B"][""]
        plantilla2["VEHICULO_B"]["CIRC12"]["ESTADO"] = datos["Circ12_B"][""]
        plantilla2["VEHICULO_B"]["CIRC13"]["ESTADO"] = datos["Circ13_B"][""]
        plantilla2["VEHICULO_B"]["CIRC14"]["ESTADO"] = datos["Circ14_B"][""]
        plantilla2["VEHICULO_B"]["CIRC15"]["ESTADO"] = datos["Circ15_B"][""]
        plantilla2["VEHICULO_B"]["CIRC16"]["ESTADO"] = datos["Circ16_B"][""]
        plantilla2["VEHICULO_B"]["CIRC17"]["ESTADO"] = datos["Circ17_B"][""]
 
        
        

    

#print(diccionario_original[mapeo['telefono_original']])
'''
diccionario_plantilla = plantilla


# Cargamos el archivo JSON con lo datos a insertar en nuestra plantilla
with open('Circ11_B.json') as f:
    diccionario_original = json.load(f)

# Actualizar diccionario_plantilla con los valores del diccionario_original
#actualizar_diccionario(diccionario_plantilla, diccionario_original, mapeo)

# Insertamos directamente a plantilla2
#modificacion_plantilla2(plantilla2, diccionario_original)



##----------------------------------------------------------------
# Guardar el diccionario_plantilla actualizado en un archivo.json
with open('archivo_mapping.json', 'w') as f:
    json.dump(diccionario_plantilla, f, indent=4)
'''
 



# Creamos una copia de la plantilla
#planti = function_load_json("plantilla.json")
#diccionario_a_modificar = planti.copy()
        

#diccionario_original = function_load_json("result_test_sdk_2.json")
#modificar_diccionario(diccionario_original, diccionario_a_modificar)




