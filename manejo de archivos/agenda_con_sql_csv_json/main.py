import pymysql
import time
import csv
import json

CONEXION = pymysql.connect(
    user="root",
    host="localhost",
    passwd="",
    database="",
    port=3306
)
cursor = CONEXION.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS `agenda`")
CONEXION.commit()

CONEXION = pymysql.connect(
    user="root",
    host="localhost",
    passwd="",
    database="agenda",
    port=3306
)
cursor = CONEXION.cursor()

try:
    cursor.execute("""
    CREATE TABLE`contactos`(
    nombre VARCHAR (50),
    numero VARCHAR (20),
    email VARCHAR(100)
                )
    """)
    print("Tabla creada correctamente")

except pymysql.MySQLError as e:
    print("Error en la base de datos:", e)

def Mostrar_menu():
    print("")
    print("")
    print("")
    print("----- Agenda -----\n")
    print("1.-Agregar contacto")
    print("2.-Eliminar contacto")
    print("3.-Buscar contacto")
    print("4.-Mostrar agenda")
    print("5.-Exportar en csv")
    print("6.-Exportar en json")
    print("7.-Salir")

def Agregar_contacto():
    nombre = input("Nombre: ")
    numero = int(input("Numero telefonico: "))
    email  = input("Email:")
    try:
        cursor = CONEXION.cursor()
        cursor.execute("INSERT INTO `contactos` (`nombre`,`numero`,`email`) VALUES (%s,%s,%s)",(nombre,numero,email))
        CONEXION.commit()
        print("Contacto guardado correctamente")
        time.sleep(2)
    except pymysql.MySQLError as e:
        print(e)

def Borrar_contacto():
    try:
        nombre = input("Nombre del contacto por eliminar: ")
        
        cursor = CONEXION.cursor()
        cursor.execute("DELETE FROM `contactos` WHERE `nombre` = %s",(nombre),)
        if cursor.rowcount == 0:
            print("Contacto no encotrado")
            time.sleep(2)
        else:
            opcion = int(input("Esta seguro de borrar el contacto: \n1.-Si\n2.-Cancelar\nOpcion: "))
            if opcion == 1:
                CONEXION.commit()
                print("Contacto borrado correctamente")
                time.sleep(2)
            else: 
                CONEXION.rollback()
                print("Eliminacion cancelada")
                time.sleep(2)



    except pymysql.err.MySQLError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def Buscar_contacto():
    nombre = input("Nombre del contacto por buscar: ")

    cursor.execute("SELECT * FROM `contactos` WHERE `nombre` = %s",(nombre),)
    resultado = cursor.fetchone()

    if resultado:
        print(f"Nombre:{resultado[0]}\nNumero:{resultado[1]}\nEmail:{resultado[2]}")
        time.sleep(3)
    else:
        print("No se encontro contacto con ese nombre")
        time.sleep(2)

def Mostrar_agenda():
    cursor.execute("SELECT * FROM `contactos`")

    resultado = cursor.fetchall()

    for contacto in resultado:
        print(f"Nombre: {contacto[0]} Numero: {contacto[1]} Email: {contacto[2]}")
        time.sleep(0.3)



def Exportar_csv():
    cursor = CONEXION.cursor()
    cursor.execute("SELECT * FROM `contactos`")
    with open("agenda.csv","w",newline="",encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([desc[0] for desc in cursor.description])
        writer.writerows(cursor.fetchall())

def Exportar_json():
    cursor = CONEXION.cursor()
    cursor.execute("SELECT * FROM `contactos`")

    columnas = [desc[0] for desc in cursor.description]
    datos = cursor.fetchall()
    listas = [dict(zip(columnas,fila))for fila in datos]

    with open("agenda.json","w",encoding="utf-8") as archivo :
        json.dump(listas,archivo,indent=4)



opcion = 0
while opcion != 7:
    Mostrar_menu()
    try:
    
        opcion = int(input("Selecione una opcion: "))
        if opcion == 1:
            Agregar_contacto()
        elif opcion == 2:
            Borrar_contacto()
        elif opcion == 3:
            Buscar_contacto()
        elif opcion == 4:
            Mostrar_agenda()
        elif opcion == 5:
            Exportar_csv()
        elif opcion == 6:
            Exportar_json()
        elif opcion == 7:
            break
        else:
            print("Opcion no valida")
    except ValueError:
        print("Seleccione la opcion con numeros")
        time.sleep(3)