

## Convertir un numero entero a decimal


num = int(input("Ingrese un numero entero: "))
binario = ""
while num > 0:
    binario = str(num % 2) + binario

    num = num //2 

print (binario)