from viajero import ViajeroFrecuente
    
with open('viajeros.csv') as archivo:
    lista_viajeros = []
    # Leer la primera línea (encabezado) y ignorarla
    archivo.readline()
    for linea in archivo:
        campos = linea.strip().split(',')
        num_viajero = int(campos[0])
        dni = int(campos[1])
        nombre = campos[2]
        apellido = campos[3]
        millas_acum = int(campos[4])
        viajero = ViajeroFrecuente(num_viajero, dni, nombre, apellido, millas_acum)
        lista_viajeros.append(viajero)
        
viajero1 = ViajeroFrecuente(1, 36253574, "Juan", "Navarro", 495)
viajero2 = ViajeroFrecuente(2, 30895360, "Maria", "Gonzalez", 1200)
viajero3 = ViajeroFrecuente(3, 27005835, "Pedro", "Lopez", 750)
viajero4 = ViajeroFrecuente(4, 39124680, "Ana", "Perez", 900)

lista_viajeros.extend([viajero1, viajero2, viajero3, viajero4])

num_viajero = int(input("\nIngrese el número de viajero frecuente: "))

# Buscar el viajero en la lista
viajero = None
i = 0
while i < len(lista_viajeros):
    if lista_viajeros[i].num_viajero == num_viajero:
        viajero = lista_viajeros[i]
        break
    i += 1

if viajero is None:
    print("El número de viajero frecuente ingresado no existe.")

while True:
    opcion = input("\n Seleccione una opción:\n a- Consultar Cantidad de Millas.\n b- Acumular Millas.\n c- Canjear Millas.\n x- Salir.\n")
    if opcion == 'a':
        print("\n El total acumulado de millas hasta ahora es ", viajero.cantidadTotalMillas())
    elif opcion == 'b':
        cantidad = int(input("\n Ingrese las millas adicionales: "))
        viajero.acumularMillas(cantidad)
    elif opcion == 'c':
        cantidad = int(input("\n Ingrese las millas que desea canjear: "))
        viajero.canjearMillas(cantidad)
    elif opcion == 'x':
        break
    else:
        print("Opción inválida.")
