class Registro:
    def __init__(self, temperatura, humedad, presion):
        self.temperatura = temperatura
        self.humedad = humedad
        self.presion = presion

class RegistroClima:
    def __init__(self):
        self.registros = [[None for j in range(24)] for i in range(31)]
    
    def cargar_datos(self, archivo):
        with open(archivo, 'r') as file:
            for linea in file:
                datos = linea.strip().split(',')
                dia = int(datos[0]) - 1
                hora = int(datos[1])
                temperatura = float(datos[2])
                humedad = float(datos[3])
                presion = float(datos[4])
                registro = Registro(temperatura, humedad, presion)
                self.registros[dia][hora] = registro
    
    def temperatura_max_min(self):
        max_presion = self.registros[0][0].presion
        max_presion_dia = 1
        max_presion_hora = 0
        min_presion = self.registros[0][0].presion
        min_presion_dia = 1
        min_presion_hora = 0
        for dia in range(31):
            for hora in range(24):
                if self.registros[dia][hora] is not None:
                    temperatura = self.registros[dia][hora].temperatura
                    if temperatura > max_temperatura:
                        max_temperatura = temperatura
                        max_temperatura_dia = dia + 1
                        max_temperatura_hora = hora
                    if temperatura < min_temperatura:
                        min_temperatura = temperatura
                        min_temperatura_dia = dia + 1
                        min_temperatura_hora = hora
        return (max_temperatura, max_temperatura_dia, max_temperatura_hora, min_temperatura, min_temperatura_dia, min_temperatura_hora)
    
    def humedad_max_min(self):
        max_humedad = self.registros[0][0].humedad
        max_humedad_dia = 1
        max_humedad_hora = 0
        min_humedad = self.registros[0][0].humedad
        min_humedad_dia = 1
        min_humedad_hora = 0
        for dia in range(31):
            for hora in range(24):
                if self.registros[dia][hora] is not None:
                    humedad = self.registros[dia][hora].humedad
                    if humedad > max_humedad:
                        max_humedad = humedad
                        max_humedad_dia = dia + 1
                        max_humedad_hora = hora
                    if humedad < min_humedad:
                        min_humedad = humedad
                        min_humedad_dia = dia + 1
                        min_humedad_hora = hora
        return (max_humedad, max_humedad_dia, max_humedad_hora, min_humedad, min_humedad_dia, min_humedad_hora)
    
    def presion_max_min(self):
        max_presion = self.registros[0][0].presion
        max_presion_dia = 1
        max_presion_hora = 0
        min_pres
       class RegistroClima:
    # código anterior
    def presion_max_min(self):
        max_presion = self.registros[0][0].presion
        max_presion_dia = 1
        max_presion_hora = 0
        min_presion = self.registros[0][0].presion
        min_presion_dia = 1
        min_presion_hora = 0
        for dia in range(31):
            for hora in range(24):
                if self.registros[dia][hora] is not None:
                    presion = self.registros[dia][hora].presion
                    if presion > max_presion:
                        max_presion = presion
                        max_presion_dia = dia + 1
                        max_presion_hora = hora
                    if presion < min_presion:
                        min_presion = presion
                        min_presion_dia = dia + 1
                        min_presion_hora = hora
        return (max_presion, max_presion_dia, max_presion_hora, min_presion, min_presion_dia, min_presion_hora)
