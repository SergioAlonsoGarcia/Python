"""
Hacer una funcion que cambie las vocales por otro caracter


"""
vocales = ["a","e","i","o","u"]


def cambiar_vocales(msg):
    msg = msg.lower()
    nuevo_msg=""
    for char in msg:
        if char in vocales:
            nuevo_msg+="*"
        else:
            nuevo_msg+=char
    return nuevo_msg


print(cambiar_vocales("Hola mundo"))