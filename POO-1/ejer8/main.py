from conjunto import Conjunto

def test():
    # Creamos algunos conjuntos de prueba
    A = Conjunto([1, 2, 3, 4])
    B = Conjunto([3, 6, 9])
    C = Conjunto([2, 4, 6, 8])

    # Realizamos algunas operaciones de prueba
    print("Unión de A y B:", A + B)
    print("Diferencia de A y B:", A - B)
    print("Diferencia de B y A:", B - A)
    print("Igualdad de A y C:", A == C)
    print("Igualdad de B y C:", B == C)
    print("Igualdad de A y A:", A == A)

def main():
    # Creamos los conjuntos a partir de los valores ingresados por el usuario
    A = Conjunto(input("Ingrese los elementos del conjunto A separados por comas: "))
    B = Conjunto(input("Ingrese los elementos del conjunto B separados por comas: "))

    # Mostramos el menú de opciones al usuario
    while True:
        print("\n--- Menú de opciones ---")
        print("1. Unión de conjuntos")
        print("2. Diferencia de conjuntos")
        print("3. Verificar igualdad de conjuntos")
        print("4. Salir")

        # Leemos la opción elegida por el usuario
        opcion = input("Ingrese una opción (1-4): ")

        # Realizamos la operación correspondiente según la opción elegida
        if opcion == "1":
            print("Unión de conjuntos:", A + B)
        elif opcion == "2":
            print("Diferencia de conjuntos (A - B):", A - B)
            print("Diferencia de conjuntos (B - A):", B - A)
        elif opcion == "3":
            if A == B:
                print("Los conjuntos A y B son iguales")
            else:
                print("Los conjuntos A y B son distintos")
        elif opcion == "4":
            break
        else:
            print("Opción inválida, por favor intente de nuevo")

if __name__ == '__main__':
    test()
    main()
