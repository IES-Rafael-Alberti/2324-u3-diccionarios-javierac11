from src.Ejercicio7 import generarLista, generarMensaje, clacularTotal

datos_leedatos = ["0", 1.45, "Platanos", 5.89, "Pollo"]

def mock_leedato(s):
    return datos_leedatos.pop()

def test_leeCliente(monkeypatch):
    monkeypatch.setattr("builtins.input", mock_leedato)
    assert generarLista() == {'Pollo': 5.89, "Platanos": 1.45}
    
def test_calcularTotal():
    assert(clacularTotal({'Pollo': 5.89, "Platanos": 1.45})) == 7.34
    
def test_generaMensaje():
    assert generarMensaje({'Pollo': 5.89, "Platanos": 1.45}, 7.34) == "Lista de la compra\nPollo\t5.89\nPlatanos\t1.45\nTotal\t7.34"