from src.Ejercicio1 import devuelveSimbolo

def test_devuelveSimbolo():
    assert devuelveSimbolo("Yen", {"Euro": "€", "Dollar": "$", 'Yen': '¥'}) == "¥"