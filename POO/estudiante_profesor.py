"""
🧠 Ejercicio 1: Universidad con Estudiantes y Profesores
- Crea una clase base Persona con atributos nombre y edad.
- Crea dos clases hijas: Estudiante y Profesor.
- Estudiante tendrá atributos adicionales: matricula, carrera.
- Profesor tendrá: id_empleado, materia.
- Ambos deben tener un método presentarse() personalizado.
- Crea una lista con 3 objetos Estudiante y 2 objetos Profesor y haz que todos se presenten usando un bucle.
"""

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

class Estudiante(Persona):
    def __init__(self, nombre, edad,matricula,carrera):
        super().__init__(nombre, edad)

        self.matricula = matricula
        self.carrera = carrera

    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años de edad")

