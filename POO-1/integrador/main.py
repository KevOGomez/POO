from alumnos import Alumno, ManejadorAlumnos
from materias import MateriaAprobada, ManejadorMaterias
import os

# Funciones auxiliares
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("---- MENÚ DE OPCIONES ----")
    print("1. Informar promedio de un alumno")
    print("2. Informar alumnos que aprobaron una materia en forma promocional")
    print("3. Listar alumnos ordenados por año y apellido/nombre")
    print("0. Salir")

def cargar_alumnos(man_alumnos):
    try:
        with open("alumnos.csv", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                dni = int(datos[0])
                apellido = datos[1]
                nombre = datos[2]
                carrera = datos[3]
                anio_cursa = int(datos[4])
                alumno = Alumno(dni, apellido, nombre, carrera, anio_cursa)
                man_alumnos.agregar_alumno(alumno)
    except FileNotFoundError:
        print("ERROR: No se encontró el archivo alumnos.csv")

def cargar_materias(man_materias):
    try:
        with open("materiasAprobadas.csv", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                dni = int(datos[0])
                materia = datos[1]
                fecha = datos[2]
                nota = float(datos[3])
                aprobacion = datos[4]
                materia_aprobada = MateriaAprobada(dni, materia, fecha, nota, aprobacion)
                man_materias.agregar_materia(materia_aprobada)
    except FileNotFoundError:
        print("ERROR: No se encontró el archivo materiasAprobadas.csv")

def informar_promedio(man_alumnos):
    dni = int(input("Ingrese el DNI del alumno: "))
    opcion = input("¿Desea incluir los aplazos en el cálculo del promedio? (S/N): ")
    if opcion.lower() == "s":
        promedio = man_alumnos.promedio_con_aplazos(dni)
    else:
        promedio = man_alumnos.promedio_sin_aplazos(dni)
    if promedio is None:
        print("No se encontró el alumno con DNI", dni)
    else:
        print("Promedio:", promedio)

def informar_aprobados(man_materias):
    materia = input("Ingrese el nombre de la materia: ")
    nota_minima = float(input("Ingrese la nota mínima para aprobar la materia en forma promocional: "))
    aprobados = man_materias.aprobados_promocion(materia, nota_minima)
    if not aprobados:
        print("No se encontraron estudiantes que aprobaran la materia en forma promocional")
    else:
        print("DNI\t\tApellido y nombre\t\tFecha\t\tNota\tAño que cursa")
        for alumno in aprobados:
            print(f"{alumno.dni}\t{alumno.apellido}, {alumno.nombre}\t{alumno.fecha.strftime('%d/%m/%Y')}\t{alumno.nota
def listar_alumnos(man_alumnos):
    alumnos_ordenados = man_alumnos.listar_alumnos_ordenados()
    if not alumnos_ordenados:
        print("No se encontraron alumnos")
    else:
        print("DNI\t\tApellido y nombre\t\tCarrera\t\tAño que cursa")
        for alumno in alumnos_ordenados:
            print(f"{alumno.dni}\t{alumno.apellido}, {alumno.nombre}\t{alumno.carrera}\t\t{alumno.anio_cursa}")

# Creación de los objetos manejadores y carga de datos
man_alumnos = ManejadorAlumnos()
man_materias = ManejadorMaterias()
cargar_alumnos(man_alumnos)
cargar_materias(man_materias)

# Ejecución del programa
while True:
    limpiar_pantalla()
    mostrar_menu()
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        informar_promedio(man_alumnos)
    elif opcion == "2":
        informar_aprobados(man_materias)
    elif opcion == "3":
        listar_alumnos(man_alumnos)
    elif opcion == "0":
        break
    else:
        print("Opción inválida")
    input("Presione Enter para continuar...")