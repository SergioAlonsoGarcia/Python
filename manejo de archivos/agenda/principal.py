def mostrarMenu():
    print("\n--- Agenda De Contactos --- \n")
    print("1.-Ver contactos")
    print("2.-Agregar contacto")
    print("3.-Buscar contacto")
    print("4.-Salir")

def verContactos():
    try:
        with open("agenda.txt","r") as archivo :
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print("Aun no existe la agenda")

def agregarContacto():
    nombre = input("Nombre: ")
    numero = input("Numero: ")
    email = input("Email: ")
    with open("agenda.txt","a") as archivo :
        archivo.write(f"Nombre: {nombre}, Telefono: {numero}, Email: {email}\n")
    print("Contacto guardado")

def buscarContacto():
    nombre = input("Nombre del contacto: ").lower()
    try:
        with open("agenda.txt","r") as archivo :
            for linea in archivo:
                if nombre in linea.lower():
                    print("")
                    print(linea.strip())
    except FileNotFoundError:
        print("Aun no existe la agenda")

while True:
    mostrarMenu()
    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        verContactos()
    elif opcion == "2":
        agregarContacto()
    elif opcion == "3":
        buscarContacto()
    elif opcion == "4":
        print("Hasta luego")
        break
    else:
        print("¡Error! Opcion no dispoible")