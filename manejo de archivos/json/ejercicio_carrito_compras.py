import json

with open("carrito.json","r") as file :
    productos = json.load(file)

total = 0

for articulo in productos:
    precio = articulo["cantidad"] * articulo["precio"]
    total+=precio

    print(f"{articulo["nombre"]} = {precio}")

print(f"\nTotal = {total}")