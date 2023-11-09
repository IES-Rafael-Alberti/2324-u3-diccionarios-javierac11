from src.Ejercicio10 import pedirDatos, aniadirUsuario, comprobarUsuario, eliminarCliente, usuariosPreferente

datos_leedatos = ["s", "jacecas@g.educaand.es", "677895852", "Cádiz", "Javier"]

def mock_leedato(s):
    return datos_leedatos.pop()

def test_pedirdatos(monkeypatch):
    monkeypatch.setattr("builtins.input", mock_leedato)
    assert pedirDatos() == {"nombre": "Javier", "direccion": "Cádiz", "telefono": "677895852", "correo": "jacecas@g.educaand.es", "preferente": True}
    
def test_aniadirUsuario():
    datos = [{"nombre": "Javier"}, {"direccion": "Cádiz"}, {"telefono": "677895852"}, {"correo": "jacecas@g.educaand.es"}, {"preferente": True}]
    assert aniadirUsuario({}, "789789745", datos) == {"789789745": [{"nombre": "Javier"}, {"direccion": "Cádiz"}, {"telefono": "677895852"}, {"correo": "jacecas@g.educaand.es"}, {"preferente": True}]}
    
def test_comprobarUsuario():
    usuarios = {"789789745": [{"nombre": "Javier"}, {"direccion": "Cádiz"}, {"telefono": "677895852"}, {"correo": "jacecas@g.educaand.es"}, {"preferente": True}]}
    assert comprobarUsuario(usuarios, "789789745") == True
    assert comprobarUsuario(usuarios, "78978974") == False
    
def test_EliminaCLiente():
    usuarios = {"789789745": [{"nombre": "Javier"}, {"direccion": "Cádiz"}, {"telefono": "677895852"}, {"correo": "jacecas@g.educaand.es"}, {"preferente": True}]}
    assert eliminarCliente(usuarios, "789789745") == {}
    
def test_usuariosPreferentes():
    usuarios = {"77177898": {"nombre": "Javier", "direccion": "Cádiz", "telefono": "677895852", "correo": "jacecas@g.educaand.es", "preferente": True}}
    assert usuariosPreferente(usuarios) == usuarios
    