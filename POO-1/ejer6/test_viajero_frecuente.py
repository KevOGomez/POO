from viajero_frecuente import ViajeroFrecuente

def test():
    # Creación de instancias de ViajeroFrecuente
    viajero1 = ViajeroFrecuente(123, "11111111", "Juan", "Perez", 1000)
    viajero2 = ViajeroFrecuente(456, "22222222", "Pedro", "Garcia", 5000)
    viajero3 = ViajeroFrecuente(789, "33333333", "Luis", "Martinez", 2500)

    # Verificación del método de acumular millas
    viajero1.acumularMillas(500)
    assert viajero1.millas_acum == 1500

    # Verificación de la sobrecarga del operador relacional mayor
    assert viajero2 > viajero1
    assert viajero2 > viajero3
