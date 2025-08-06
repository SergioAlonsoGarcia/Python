import pandas as pd

"""
    Muestra la "tabla"
df= pd.read_csv("alumnos.csv")
print(df)
"""
df= pd.read_csv("alumnos.csv")
buenos_alumnos = df[df["calificacion"]>=8]
print(buenos_alumnos)

# Crea un nuevo csv con esos datos
buenos_alumnos.to_csv("alumnos_destacados.csv",index=False)