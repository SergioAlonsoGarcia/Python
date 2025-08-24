import os
from pathlib import Path, PurePath


# OBTENER RUTA
# print(os.getcwd())  #string
# print(Path.cwd())   #"clase"


# LISTAR ARCHIVOS 
# print(os.listdir())
# print(os.listdir("carpeta prueba"))

# print(list(Path().iterdir()))
# print(list(Path("carpeta_prueba").iterdir()))

# CONCATECAR 'RUTA'
# print(os.path.join(os.getcwd(),"carpeta_prueba"))
# print(PurePath.joinpath(Path.cwd(),"carpeta_prueba"))


# CREAR CARPETAS
# os.mkdir("carpeta")
# Path("carpeta").mkdir(exist_ok=True) # EVITA ERROR SI EXISTE

# os.makedirs(os.path.join("carpeta1","carpeta2"))
# PurePath.joinpath(Path.cwd(),"carpeta1","carpeta2").mkdir(parents=True) # PERMITE CREAR SUBCARPETAS

# RENOMBRAR
# os.rename("carpeta1","scripts")

# path_actual = Path ("scripts")
# path_final = Path ("carpeta")

# Path.rename(path_actual,path_final)

"""
for file in os.listdir():
    if file.endswith(".txt"):
        os.rename(file,f"2025_{file}")
"""

# VERIFICAR SI EXISTE
# print(os.path.exists("carpeta"))

# archivo = Path ("carpeta1")
# print(archivo.exists())

# METADATA
# print(os.path.abspath("carpeta"))

script = Path("pruebas.py")

print(script.resolve())
print(script.stem) # nombre del archivo
print(script.suffix) # extencion del archivo
print(script.stat().st_size)