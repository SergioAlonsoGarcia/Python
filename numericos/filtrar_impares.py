"""
Hacer una funcion que filtre numeros impares de una lista


"""

def filtro_impares(lista):
    nueva_lista=[]
    for num in lista:
        if num % 2 == 1 :
            nueva_lista.append(num)
    return nueva_lista

print(filtro_impares([1,2,3,4,5,6,7,8,9])) # Salida 1,3,5,7,9