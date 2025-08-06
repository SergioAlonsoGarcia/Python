import csv
import matplotlib.pyplot as plt


valores = []
with open ("graficar.csv","r",newline="") as file:
    leer = csv.reader(file)

    for row in leer:
        valor = int(row[0])
        valores.append(valor)

    plt.style.use("seaborn-v0_8-dark")
    fig , ax = plt.subplots()
    ax.plot(valores,c="blue")
    plt.show()

# print(plt.style.available)

