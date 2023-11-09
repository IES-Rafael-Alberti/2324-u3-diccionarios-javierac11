#Ejercicio 3.2.3¶
#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta,
#un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario 
#debe mostrar un mensaje informando de ello.
"""
Fruta 	Precio
Plátano 	1.35
Manzana 	0.80
Pera 	0.85
Naranja 	0.70
"""

def leeFruta():
    fruta = input("Introduce una fruta: ")
    return fruta

def leeKilos():
    try:
        kilos = input("Introduce la cantidad de kilos: ")
        kilos = float(kilos)
        return kilos
    except:
        raise ValueError
    
def compruebaFruta(frutas, fruta):
    if fruta in frutas:
        return True
    else:
        return False
    
def claculaPrecioTotal(frutas, fruta, kilos):
    precio = frutas[fruta] 
    precio_total = precio * kilos
    return precio_total

if __name__ == '__main__':
    frutas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}
    fruta = leeFruta()
    if compruebaFruta(frutas, fruta):
        kilos = leeKilos()
        print(claculaPrecioTotal(frutas, fruta, kilos))
    else:
        print("La futa no existe")