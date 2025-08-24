import os 
try:
    for i in range(5):
        with open(f"archivo{i}.txt","w") as archivo:
            archivo.write("Hola mundo")

    print("Archivos creados correctamente ✅")
except FileNotFoundError:
    print("El archivo no existe")
    


for file in os.listdir():
    if file.endswith(".txt"):
        os.rename(file,f"{file}_2025")