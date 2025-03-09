"""
Hacer una funcion que cuente el numero de vocales de una oracion


"""

vocales = ["a","e","i","o","u"]

def contar_vocales(msg):
    contador = 0
    msg =msg.lower()
    for char in msg:
        if char in vocales:
            contador+=1
    print(contador)


contar_vocales("Hola mundo")
contar_vocales("bcdf")