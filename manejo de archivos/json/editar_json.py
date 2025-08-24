import json

with open ("carrito.json","r") as file:
    productos = json.load(file)


for producto in productos:
    if producto["nombre"] == "manzanas":
        producto["precio"] = 10
        producto["cantidad"] = 12


with open ("carrito.json","w") as file:
    json.dump(productos,file, indent=4, ensure_ascii=False)