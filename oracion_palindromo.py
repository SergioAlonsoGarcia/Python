"""
Hacer una funcion que verifique si una frase es palindromo

"Anita lava la tina"
"""


def palindromo(msg):
    msg ="".join(msg.lower().split())

    return msg == msg[::-1]


print(palindromo("Anita lava la tina"))
print(palindromo("Amor a Roma"))
print(palindromo("Hola mundo"))