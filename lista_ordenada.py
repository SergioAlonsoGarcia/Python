"""
Hacer una funcion para ver si los numeros de una lista estan acomodados
de mayor a menor


"""

def verificar_orden(lista):
    for i in range (len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True


print(verificar_orden([1,2,3,4,5,6,7]))
print(verificar_orden([1,3,2,4,6,5,7]))