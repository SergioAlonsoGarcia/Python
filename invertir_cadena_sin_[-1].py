"""
Hacer una funcion que invierta una cadena sin usar [::-1]


"""

def invertir_cadena(msg):
    invertida = ""
    for char in msg:
        invertida=char+invertida
    return invertida

print(invertir_cadena("Hola mundo")) # Salida odnum aloH