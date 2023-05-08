from emails import Email

# 1- Ingresar el nombre de una persona y su dirección de e-mail
nombre = input("Ingrese su nombre: ")
idCuenta = input("Ingrese su id de cuenta: ")
dominio = input("Ingrese su dominio: ")
tipoDominio = input("Ingrese su tipo de dominio: ")
contrasena = input("Ingrese su contraseña: ")

miEmail = Email(idCuenta, dominio, tipoDominio, contrasena)
print(f"Estimado {nombre}, te enviaremos tus mensajes a la dirección {miEmail.retornaEmail()}.")

# 2- Modificar la contraseña
contrasenaActual = input("Ingrese su contraseña actual: ")
if contrasenaActual == miEmail.contrasena:
    nuevaContrasena = input("Ingrese su nueva contraseña: ")
    miEmail.contrasena = nuevaContrasena
    print("Contraseña modificada con éxito.")
else:
    print("Contraseña incorrecta.")

# 3- Crear un objeto de clase Email a partir de una dirección de correo
direccion = input("Ingrese una dirección de correo: ")
nuevoEmail = Email("", "", "", "")
nuevoEmail.crearCuenta(direccion)
print(f"Se ha creado una nueva cuenta con id de cuenta {nuevoEmail.idCuenta}, dominio {nuevoEmail.dominio} y tipo de dominio {nuevoEmail.tipoDominio}.")

# 4- Leer direcciones de email desde un archivo y crear cuentas
emails = []
with open('emails.csv', 'r') as f:
    lineas = f.readlines()
    for linea in lineas:
        email = Email("", "", "", "")
        email.crearCuenta(linea.strip())
        emails.append(email)

dominioBuscado = input("Ingrese un dominio para buscar: ")
contador = 0
for email in emails:
    if email.getDominio() == dominioBuscado:
        contador += 1

print(f"Se encontraron {contador} emails con el dominio {dominioBuscado}.")