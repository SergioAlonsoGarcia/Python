import pandas as pd

df = pd.read_csv("alumnos.csv")

df["estatus"] = df["calificacion"].apply(lambda x: "Aprobado" if x >= 8 else "Reprobado")

print(df)

promedio = df["calificacion"].mean()
print(f"Calificacion promedio:{promedio}")