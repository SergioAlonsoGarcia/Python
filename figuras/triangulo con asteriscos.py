"""

    Funcion que pida un numero y imprima un triangulo de esa altura
"""

def triangulo(num):
    espacio = " "
    cosa = num
        # print(f"{" * "*i} \n")
    for i in range (1,num+1):
        if i == 1:
            print(f"{espacio * (num -1)} * {espacio * (num-1)}")
        else:
            print(f"{(cosa - i)*espacio}{" *"*i}{(cosa - i)*espacio}")
    

triangulo(5)