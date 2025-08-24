import os 
from pathlib import Path 


# os.remove("archivo0.txt")

archivo = Path("archivo1.txt")
Path.unlink(archivo)


# Para carpetas vacías os.rmdir("carpeta").
# Para carpetas con contenido shutil.rmtree("carpeta").<


# Para carpetas completas shutil.rmtree(Path("carpeta")).