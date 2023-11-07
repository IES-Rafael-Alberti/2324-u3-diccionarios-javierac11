from src.Ejercicio5 import generaMensajes

def test_generaMensajes():
    assert generaMensajes({"Prog": 7, "DAW": 8, "LLMM": 6}) == ["Prog tiene 7", "DAW tiene 8", "LLMM tiene 6"]