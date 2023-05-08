class ViajeroFrecuente:
    def __init__(self, num_viajero, dni, nombre, apellido, millas_acum):
        self.num_viajero = num_viajero
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.millas_acum = millas_acum
    
    def cantidadTotalMillas(self):
         return self.millas_acum
    
    def acumularMillas(self, cantidad):
        self.millas_acum += cantidad
        
    def canjearMillas(self, cantidad):
        if cantidad <= self.millas_acum:
            print ("\n Puede canjear sus millas")
            self.millas_acum -= cantidad
        else:
            print ("\nError en la operación: ha ingresado un numero demasiado elevado")
            print ("Secuencia de autodestrucción activada \n")
    
    # Sobrecarga de operador ==
    def __eq__(self, other):
        return self.millas_acum == other
    
    # Sobrecarga de operador +
    def __radd__(self, other):
        self.millas_acum += other
        return self
    
    # Sobrecarga de operador -
    def __rsub__(self, other):
        self.millas_acum -= other
        return self
