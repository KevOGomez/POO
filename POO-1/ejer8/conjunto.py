class Conjunto:
    def __init__(self, conjunto):
        if not all(isinstance(x, int) for x in conjunto):
            raise TypeError("El conjunto debe contener solo números enteros")
        self.conjunto = set(conjunto)

    def __str__(self):
        return "{" + ", ".join(str(x) for x in self.conjunto) + "}"

    def __add__(self, other):
        if not isinstance(other, Conjunto):
            raise TypeError("El segundo operando debe ser un conjunto")
        return Conjunto(self.conjunto | other.conjunto)

    def __sub__(self, other):
        if not isinstance(other, Conjunto):
            raise TypeError("El segundo operando debe ser un conjunto")
        return Conjunto(self.conjunto - other.conjunto)

    def __eq__(self, other):
        if not isinstance(other, Conjunto):
            return False
        return self.conjunto == other.conjunto
