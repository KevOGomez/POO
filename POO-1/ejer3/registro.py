class Registro:
    def __init__(self, temperatura=0, humedad=0, presion=0):

        self.temperatura = temperatura
        self.humedad = humedad
        self.presion = presion

    def __str__(self):
 
        return f"temperatura: {self.temperatura}, humedad: {self.humedad}, presión: {self.presion}"
