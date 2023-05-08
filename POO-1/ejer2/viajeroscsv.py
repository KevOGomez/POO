import csv
import random

nombres = ["Juan", "Pedro", "Maria", "Ana", "Luis", "Carla", "Federico", "Lucia", "Sofia", "Jorge"]
apellidos = ["Garcia", "Perez", "Martinez", "Gonzalez", "Lopez", "Fernandez", "Rodriguez", "Sanchez", "Diaz", "Torres"]

with open("viajeros.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(["num_viajero", "dni", "nombre", "apellido", "millas_acum"])
    for i in range(10):
        num_viajero = i+1
        dni = random.randint(10000000, 99999999)
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        millas_acum = random.randint(100, 1000)
        writer.writerow([num_viajero, dni, nombre, apellido, millas_acum])
