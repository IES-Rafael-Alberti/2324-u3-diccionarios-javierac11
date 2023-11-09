from src.Ejercicio4 import generaMensaje

def test_generaMensaje():
    assert generaMensaje("11/04/2003") == "11 de Abril de 2003"