#Ejercicio 3.2.7¶
#Escribir un programa que cree un diccionario simulando una cesta de la compra. 
#El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar.
#Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
"""
Lista de la compra 	
Artículo 1 	Precio
Artículo 2 	Precio
Artículo 3 	Precio
… 	…
Total 	Coste
"""

def pedirArticulo():
    articulo = input("Introduce un articulo o \"0\" para salir: ")
    return articulo
    
def pedirPrecio():
    precio = input("Introduce el precio del articulo: ")
    try:
        precio = float(precio)
        return precio
    except:
        raise ValueError

def generarLista():
    lista = {}
    articulo = pedirArticulo()
    while articulo != "0":
        precio = pedirPrecio()
        lista[articulo] = precio
        articulo = pedirArticulo()
    return lista

def clacularTotal(lista):
    total = 0
    for articulo in lista:
        total += lista[articulo]
    return total

def generarMensaje(lista, total):
    mensaje = "Lista de la compra"
    for articulo in lista:
        mensaje += f"\n{articulo}\t{lista[articulo]}"
    mensaje += f"\nTotal\t{total}" 
    return mensaje
    
    
if __name__ == '__main__':
    try:
        articulos = generarLista()
        total = clacularTotal(articulos)
        print(generarMensaje(articulos, total))
    except:
        print("Error")