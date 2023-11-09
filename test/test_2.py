from src.Ejercicio2 import generaMensaje, leeDatos, pedirEdad

datos_leedatos = ["20", "676789652", "Cádiz", "Javier"]

def mock_leedato(s):
    return datos_leedatos.pop()

def test_pedirEdad(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "20")
    assert pedirEdad() == 20

def test_leedatos(monkeypatch):
    monkeypatch.setattr("builtins.input", mock_leedato)
    assert leeDatos() == {'direccion': 'Cádiz', 'edad': 20, 'nombre': 'Javier', 'telefono': '676789652'}
    
def test_generaMensaje():
    assert generaMensaje({'direccion': 'Cádiz', 'edad': 20, 'nombre': 'Javier', 'telefono': '676789652'}) == "Javier tiene 20 años, vive en Cádiz y su número de teléfono es 676789652"