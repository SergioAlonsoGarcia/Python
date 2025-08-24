import os 
import shutil
from pathlib import Path

DESTINO_ARCHIVOS = "archivos"
DESTINO_IMAGENES = "imagenes"
DESTINO_MUSICA = "musica"

try:
    for archivo in Path(".").glob("*.txt"):
        file = os.path.join(".",archivo)
        if os.path.isfile(archivo):
            shutil.move(file,DESTINO_ARCHIVOS)

except FileNotFoundError:
    print("Archivo no encontrado")

try:
    for archivo in Path(".").glob("*"):
        if archivo.suffix.lower() == ".png" or archivo.suffix.lower() == ".jpg":
            file = os.path.join(".",archivo)
            if os.path.isfile(archivo):
                shutil.move(file,DESTINO_IMAGENES)

except FileNotFoundError:
    print("Archivo no encontrado")

try:
    for archivo in Path(".").glob("*.mp3"):
        file = os.path.join(".",archivo)
        if os.path.isfile(archivo):
            shutil.move(file,DESTINO_MUSICA)
except FileNotFoundError:
    print("Archivo no encontrado")
except Exception as e:
    print(f"No se pudo mover {archivo}: {e}")