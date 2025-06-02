"""
Hacer una funcion que remplace una palabra por otra en una cadena


"""

def remplazar_palabra(msg,palabra1,palabra2):

    return msg.replace(palabra1,palabra2)

print(remplazar_palabra("hola mundo","mundo","python")) # Salida hola python