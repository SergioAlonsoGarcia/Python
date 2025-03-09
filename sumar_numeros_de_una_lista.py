"""
Hacer una funcion que sume todos los numeros de una lista

"""

def sumar_lista(lista):
    suma=0
    for num in lista:
        suma+=num
    return suma

print(sumar_lista([1,2,3,4])) # Salida 10
print(sumar_lista([5,5,10,15])) # Salida 35