import csv
import random
import string

dominios = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
nombres = [" informatica.fcefn", "exactas.unsj", "ffha_2022", "maria", "spam", "alumnos", "deptoinformatica", "isabella", "santiago", "jose"]

def generarEmail():
    nombre = random.choice(nombres)
    dominio = random.choice(dominios)
    numero = ''.join(random.choices(string.digits, k=3))
    return f"{nombre}{numero}@{dominio}"

ruta = "/home/kevin/FACULTAD/POO/Unidad 2/ejer1/emails.csv"
with open(ruta, 'w') as f:
    writer = csv.writer(f)
    for i in range(10):
        email = generarEmail()
        writer.writerow([email])