class PlanAhorro:
    def __init__(self, codigo, modelo, version, valor, cuotas, cuotas_licitacion):
        self.codigo = codigo
        self.modelo = modelo
        self.version = version
        self.valor = valor
        self.cuotas = cuotas
        self.cuotas_licitacion = cuotas_licitacion

    def actualizar_valor(self, valor):
        self.valor = valor

    def valor_cuota(self):
        return (self.valor/self.cuotas) + (self.valor * 0.10)

    def cuotas_lic(self):
        return self.cuotas_licitacion * self.valor_cuota()

    def modificar_cuotas_licitacion(self, cuotas_licitacion):
        self.cuotas_licitacion = cuotas_licitacion
