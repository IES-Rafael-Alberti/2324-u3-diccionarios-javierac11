from src.Ejercicio8 import generaDiccionario, traduceFrase



def test_generaDiccionario():
    assert generaDiccionario(["Hola:Hello", "sol:sun", "adios:bye"]) == {"Hola": "Hello", "sol": "sun", "adios": "bye"}
    
def test_traduceFrase():
    assert traduceFrase("Hola hace sol adios", {"Hola": "Hello", "sol": "sun", "adios": "bye"}) == "Hello hace sun bye "