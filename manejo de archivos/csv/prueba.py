import csv 

datos = [
    {"first_name":"Sergio","last_name":"Garcia"},
    {"first_name":"Angel","last_name":"Oliva"}
]

fieldNames = ["first_name","last_name",""]
with open ("info.csv","w",newline="") as file:
    writer = csv.DictWriter(file,fieldnames=fieldNames)

    writer.writeheader()
    for row in datos:
        writer.writerow(row)