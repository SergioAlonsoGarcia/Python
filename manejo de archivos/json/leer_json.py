import json

with open ("persona.json","r",encoding="utf-8") as file:
    datos = json.load(file)



print(datos)
