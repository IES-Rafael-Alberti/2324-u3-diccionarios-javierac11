from src.Ejercicio3 import compruebaFruta, claculaPrecioTotal

def test_compruebaFruta():
    assert compruebaFruta({"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}, "Pera") == True
    
def test_calculaPrecioTotal():
    assert claculaPrecioTotal({"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}, "Platano", 2) == 2.7