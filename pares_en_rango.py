"""
Escribe una función que reciba dos números y devuelva la suma
 de todos los números pares entre esos dos números

Entrada: 2, 10
Salida: 30 (porque 2 + 4 + 6 + 8 + 10 = 30)

"""

def sumar_pares(num1,num2):
    suma = 0
    for i in range (num1,num2+1):
        if i %2 == 0:
            suma+=i
    return suma

print(sumar_pares(2,10))