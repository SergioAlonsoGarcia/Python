import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("alumnos.csv")

plt.bar(df["nombre"],df["calificacion"])
plt.xlabel("nombre")
plt.ylabel("calificacion")
plt.ylim(0,10)

plt.legend()
plt.show()