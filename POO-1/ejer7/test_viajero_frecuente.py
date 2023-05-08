from viajero_frecuente import ViajeroFrecuente


def test_viajero_frecuente():
    # Instancias de prueba
    vf1 = ViajeroFrecuente(1, "12345678", "Juan", "Pérez", 5000)
    vf2 = ViajeroFrecuente(2, "87654321", "María", "Gómez", 7000)
    
    # Comparación de cantidad de millas con un valor entero
    assert vf1 == 5000
    assert 6000 == vf2
    
    # Acumular millas con sobrecarga de operador +
    vf1 = 1000 + vf1
    assert vf1.cantidadTotalMillas() == 6000
    
    # Canjear millas con sobrecarga de operador -
    vf2 = 2000 - vf2
    assert vf2.cantidadTotalMillas() == 5000
