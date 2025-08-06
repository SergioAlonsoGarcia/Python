import json

persona = {
    "nombre":"Sergio",
    "edad":17,
    "lenguajes":["python","java"]
}
with open ("persona.json","w",encoding="utf-8") as file:
    json.dump(persona,file,indent=4)