import shutil
from pathlib import Path

origen = Path("carpeta_prueba")
destino = Path("backup")
destino.mkdir(exist_ok=True)

for archivo in origen.glob("*.txt"):
    shutil.copy(archivo,destino)