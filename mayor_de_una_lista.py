"""
Hacer una funcion que imprima el numero mayor de una lista


"""

def mayor_lista(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor


print(mayor_lista([1,2,3,4,5,6,7])) # Salida 7
print(mayor_lista([1,11,3,4,5,6,9])) # Salida 11