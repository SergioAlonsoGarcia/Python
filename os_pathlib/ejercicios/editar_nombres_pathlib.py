from pathlib import Path

for archivo in Path(".").glob("*.txt"):
    nuevo_nombre = archivo.stem + "_2025" + archivo.suffix
    archivo.rename(archivo.with_name(nuevo_nombre))
