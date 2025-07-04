import psycopg2

conexion = psycopg2.connect(
    dbname = "mi_base_de_datos_4pnz" ,
    user = "mi_base_de_datos_4pnz_user" ,
    password = "FvIx7OnAjxP7d13DRbV6YRSgmQRjaBm0" ,
    host = "dpg-d1jm1ra4d50c7386pmh0-a.oregon-postgres.render.com",
    
    port = 5432
)

if conexion:
    print(conexion)
try:
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT PRIMARY KEY,
            edad INT,
            nombre TEXT 
                );

    """)
    
    conexion.commit()
    print("Tabla creada")
    cursor.close()

except psycopg2.Error as e:
    print(e,"menso")


try:
    cursor = conexion.cursor()
    cursor.execute("""
    INSERT INTO usuarios(id,edad,nombre) VALUES (1,17,'sergio')
    """)
    conexion.commit()
    print("si muy bien asi mero ")
except psycopg2.Error as e:
    print(e,"menso")