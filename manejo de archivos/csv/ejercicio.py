import csv

campos=["nombre","edad","calificacion"]
valores = [
    {"nombre":"juan","edad":18,"calificacion":7.5},
    {"nombre":"maria","edad":19,"calificacion":9.0},
    {"nombre":"pedro","edad":17,"calificacion":6.0},
    {"nombre":"luisa","edad":18,"calificacion":8.5}
]
with open ("alumnos.csv","w",newline="") as file:
    writer = csv.DictWriter(file,fieldnames=campos)
    writer.writeheader()

    for row in valores:
        writer.writerow(row)

with open ("alumnos.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if float(row["calificacion"]) >= 8 :
            print(f"Nombre:{row["nombre"]}\nEdad:{row["edad"]}\nCalificacion:{row["calificacion"]}")
