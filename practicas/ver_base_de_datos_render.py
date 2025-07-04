import psycopg2

conexion = psycopg2.connect(
    dbname = "mi_base_de_datos_4pnz" ,
    user = "mi_base_de_datos_4pnz_user" ,
    password = "FvIx7OnAjxP7d13DRbV6YRSgmQRjaBm0" ,
    host = "dpg-d1jm1ra4d50c7386pmh0-a.oregon-postgres.render.com",
    
    port = 5432
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM usuarios")

registros = cursor.fetchall()

for resultado in registros:
    print(resultado )