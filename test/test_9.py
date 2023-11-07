from src.Ejercicio9 import comprobarFactura 

def test_comprobarFactura():
    assert comprobarFactura({"00": 45, "01": 8, "02": 77}, "00") == True
    assert comprobarFactura({"00": 45, "01": 8, "02": 77}, "03") == False