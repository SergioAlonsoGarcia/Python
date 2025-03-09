"""
Hacer una funcion que elimine carecteres repetidos de una cadena


"""

def borrar_repetidos(msg):
    msg_final=""
    for char in msg:
        if char not in msg_final:
            msg_final+=char
    return msg_final

print(borrar_repetidos("abcdddddddef")) # Salida abcdef