import planes.csv
from planAhorro import PlanAhorro

def leer_planes(filename):
    """
    Lee los planes de ahorro desde un archivo y devuelve una lista de instancias de la clase PlanAhorro.
    """
    planes = []
    with open(filename, 'r') as file:
        for line in file:
            datos = line.strip().split(';')
            codigo = datos[0]
            modelo = datos[1]
            version = datos[2]
            valor = float(datos[3])
            cuotas = int(datos[4])
            cuotas_licitar = int(datos[5])
            plan = PlanAhorro(codigo, modelo, version, valor, cuotas, cuotas_licitar)
            planes.append(plan)
    return planes


def actualizar_valor(planes):
    """
    Actualiza el valor del vehículo de cada plan.
    """
    print('Actualizar valor del vehículo')
    codigo = input('Ingrese el código del plan: ')
    modelo = input('Ingrese el modelo y versión del vehículo: ')
    valor_actual = float(input('Ingrese el valor actual del vehículo: '))
    for plan in planes:
        if plan.codigo == codigo and plan.modelo == modelo:
            plan.valor = valor_actual
            print('Valor actualizado con éxito.')
            return
    print('No se encontró el plan con ese código y modelo.')


def buscar_valor_cuota(planes):
    """
    Busca los planes cuyo valor de la cuota sea inferior al valor dado.
    """
    print('Buscar planes por valor de cuota')
    valor = float(input('Ingrese el valor de la cuota: '))
    for plan in planes:
        if plan.valor_cuota() < valor:
            print(f'Código del plan: {plan.codigo}, Modelo y versión del vehículo: {plan.modelo} {plan.version}')


def monto_cuotas_licitar(planes):
    """
    Muestra el monto que se debe haber pagado para licitar el vehículo.
    """
    print('Calcular monto para licitar')
    codigo = input('Ingrese el código del plan: ')
    for plan in planes:
        if plan.codigo == codigo:
            monto = plan.valor_cuota() * plan.cuotas_licitar
            print(f'Monto a pagar para licitar: {monto:.2f}')
            return
    print('No se encontró el plan con ese código.')


def modificar_cuotas_licitar(planes):
    """
    Modifica la cantidad de cuotas que debe tener pagas para licitar el vehículo.
    """
    print('Modificar cantidad de cuotas para licitar')
    codigo = input('Ingrese el código del plan: ')
    nueva_cantidad = int(input('Ingrese la nueva cantidad de cuotas para licitar: '))
    for plan in planes:
        if plan.codigo == codigo:
            plan.cuotas_licitar = nueva_cantidad
            print('Cantidad de cuotas para licitar modificada con éxito.')
            return
    print('No se encontró el plan con ese código.')

def test():
    """
    Crea instancias de la clase PlanAhorro con datos de prueba para validar las funcionalidades del programa.
    """
    planes = [
        PlanAhorro('1', 'Peugeot', '208', 500000, 60, 36),
        PlanAhorro('2', 'Renault', 'Clio', 450000, 72, 48),
        PlanAhorro('3', 'Ford', 'Ka', 400000, 84, 60),
        PlanAhorro('4', 'Volkswagen', 'Gol', 550000, 48, 24),
        PlanAhorro('5', 'Chevrolet', 'Onix', 600000, 36, 24)
    ]

    print('\nPlanes de ahorro:')
    for plan in planes:
        print(f'Código: {plan.codigo}, Modelo y versión: {plan.modelo} {plan.version}, Valor: {plan.valor}, Cuotas: {plan.cuotas}, Cuotas para licitar: {plan.cuotas_licitar}')

    actualizar_valor(planes)

    buscar_valor_cuota(planes)

    monto_cuotas_licitar(planes)

    modificar_cuotas_licitar(planes)

    print('\nPlanes de ahorro actualizados:')
    for plan in planes:
        print(f'Código: {plan.codigo}, Modelo y versión: {plan.modelo} {plan.version}, Valor: {plan.valor}, Cuotas: {plan.cuotas}, Cuotas para licitar: {plan.cuotas_licitar}')


