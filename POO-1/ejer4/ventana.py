class Ventana:
    
    def __init__(self, titulo, xi=0, yi=0, xd=100, yd=100):
        if xi < 0:
            xi = 0
        if yi < 0:
            yi = 0
        if xd > 500:
            xd = 500
        if yd > 500:
            yd = 500
        if xi >= xd or yi >= yd:
            raise ValueError("Coordenadas inválidas")

        self.__titulo = titulo
        self.__xi = xi
        self.__yi = yi
        self.__xd = xd
        self.__yd = yd
        
    def mostrar(self):
        print("Ventana:", self.__titulo)
        print("Coordenadas Vértice Superior Izquierdo:", self.__xi, ",", self.__yi)
        print("Coordenadas Vértice Inferior Derecho:", self.__xd, ",", self.__yd)
        
    def getTitulo(self):
        return self.__titulo
    
    def alto(self):
        return self.__yd - self.__yi
    
    def ancho(self):
        return self.__xd - self.__xi
    
    def moverDerecha(self, desplazamiento=1):
        if self.__xd + desplazamiento > 500:
            self.__xd = 500
            self.__xi = self.__xd - self.ancho()
        else:
            self.__xi += desplazamiento
            self.__xd += desplazamiento
    
    def moverIzquierda(self, desplazamiento=1):
        if self.__xi - desplazamiento < 0:
            self.__xi = 0
            self.__xd = self.__xi + self.ancho()
        else:
            self.__xi -= desplazamiento
            self.__xd -= desplazamiento
        
    def bajar(self, desplazamiento=1):
        if self.__yd + desplazamiento > 500:
            self.__yd = 500
            self.__yi = self.__yd - self.alto()
        else:
            self.__yi += desplazamiento
            self.__yd += desplazamiento
    
    def subir(self, desplazamiento=1):
        if self.__yi - desplazamiento < 0:
            self.__yi = 0
            self.__yd = self.__yi + self.alto()
        else:
            self.__yi -= desplazamiento
            self.__yd -= desplazamiento
