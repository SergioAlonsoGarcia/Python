"""

    Decimal a hexadecimal
"""
hexadecimal=("0123456789abcdef")

num = int(input("Ingresa un numero: "))
final = ""
while num > 0 :
    residuo = num % 16
    final = hexadecimal[residuo] + final
    num = num // 16


print(final)