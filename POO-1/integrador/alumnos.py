import numpy as np

class Alumno:
    def __init__(self, dni, apellido, nombre, carrera, anio):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.carrera = carrera
        self.anio = anio

    def __str__(self):
        return f"{self.dni}, {self.apellido}, {self.nombre}, {self.carrera}, {self.anio}"


class ManejadorAlumnos:
    def __init__(self, cant_alumnos):
        self.alumnos = np.empty(cant_alumnos, dtype=object)
        self.tope = 0

    def agregar_alumno(self, alumno):
        self.alumnos[self.tope] = alumno
        self.tope += 1

    def buscar_alumno(self, dni):
        for alumno in self.alumnos:
            if alumno.dni == dni:
                return alumno
        return None

    def promedio_con_aplazos(self, dni):
        alumno = self.buscar_alumno(dni)
        if alumno is None:
            return None

        notas = []
        for materia in ManejadorMaterias.materias:
            if materia.dni == dni:
                notas.append(materia.nota)
        if len(notas) == 0:
            return None

        promedio = sum(notas) / len(notas)
        return promedio

    def promedio_sin_aplazos(self, dni):
        alumno = self.buscar_alumno(dni)
        if alumno is None:
            return None

        notas = []
        for materia in ManejadorMaterias.materias:
            if materia.dni == dni and materia.nota >= 4:
                notas.append(materia.nota)
        if len(notas) == 0:
            return None

        promedio = sum(notas) / len(notas)
        return promedio

    def ordenar_por_anio_y_apellido(self):
        self.alumnos = sorted(self.alumnos, key=lambda alumno: (alumno.anio, alumno.apellido, alumno.nombre))

    def __str__(self):
        s = ""
        for alumno in self.alumnos:
            s += str(alumno) + "\n"
        return s
