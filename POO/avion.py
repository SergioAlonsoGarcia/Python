"""
🔧 Ejercicio: Clase Avión
Crea una clase llamada Avion que herede de una clase base VehiculoAereo. 
La clase base debe tener atributos comunes como compañia y capacidad. 
En la clase Avion, añade un atributo adicional que indique la cantidad de motores.
 Además, implementa un método específico llamado despegar() que imprima
un mensaje como “El avión está despegando”.
"""

class VehiculoAereo:
    def __init__(self,compañia,capacidad):
        self.compañia = compañia
        self.capacidad = capacidad

    def describir(self):
        print(f"Vehiculo aereo compañia {self.compañia} de capacidad {self.capacidad}")


class Avion(VehiculoAereo):
    def __init__(self, compañia, capacidad,motores):
        super().__init__(compañia, capacidad)
        self.motores = motores

    def despegar(self):
        print(f"El avion esta despegando")

avion1 = Avion("Aerobus",200,4)
avion1.describir()
avion1.despegar()