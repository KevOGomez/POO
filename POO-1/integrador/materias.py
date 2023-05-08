from datetime import datetime

class MateriaAprobada:
    def __init__(self, dni, nombre, fecha, nota, aprobacion):
        self.dni = dni
        self.nombre = nombre
        self.fecha = datetime.strptime(fecha, '%d/%m/%Y').date()
        self.nota = float(nota)
        self.aprobacion = aprobacion

class ManejadorMaterias:
    def __init__(self):
        self.materias = []

    def agregarMateria(self, materia):
        self.materias.append(materia)

    def buscarMaterias(self, nombre, notaMinima=7):
        listaMaterias = []
        for materia in self.materias:
            if materia.nombre == nombre and materia.aprobacion == 'P' and materia.nota >= notaMinima:
                listaMaterias.append(materia)
        return listaMaterias

    def __lt__(self, otro):
        return self.materias[0].fecha < otro.materias[0].fecha
