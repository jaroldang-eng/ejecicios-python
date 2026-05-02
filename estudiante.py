class Estudiante:
    def __init__(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def aprobado(self):
        return self.promedio() >= 61


# Prueba
est = Estudiante("Juan", "123", "Sistemas")
est.agregar_nota(70)
est.agregar_nota(80)

print("Promedio:", est.promedio())
print("¿Aprobado?:", est.aprobado())
