class Email:
    def __init__(self, idCuenta, dominio, tipoDominio, contrasena):
        self.idCuenta = idCuenta
        self.dominio = dominio
        self.tipoDominio = tipoDominio
        self.contrasena = contrasena

    def retornaEmail(self):
        return f"{self.idCuenta}@{self.dominio}.{self.tipoDominio}"

    def getDominio(self):
        return self.dominio

    def crearCuenta(self, direccion):
        partes = direccion.split('@')
        if len(partes) != 2:
            print("Dirección de correo inválida")
            return
        self.idCuenta = partes[0]
        dominioPartes = partes[1].split('.')
        if len(dominioPartes) != 2:
            print("Dirección de correo inválida")
            return
        self.dominio = dominioPartes[0]
        self.tipoDominio = dominioPartes[1]