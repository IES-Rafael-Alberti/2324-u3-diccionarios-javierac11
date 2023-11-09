from src.Ejercicio6 import pedirCliente

datos_leedatos = [ "jacecas@g.educaand.es", "676789652", "Masculino", "20", "Javier"]

def mock_leedato(s):
    return datos_leedatos.pop()

def test_leeCliente(monkeypatch):
    monkeypatch.setattr("builtins.input", mock_leedato)
    assert pedirCliente() == {'nombre': 'Javier', 'edad': 20, 'sexo': 'Masculino', 'telefono': '676789652', 'correo': 'jacecas@g.educaand.es'}