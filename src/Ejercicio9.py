#Ejercicio 3.2.9¶
#Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
#Las facturas se almacenarán en un diccionario donde la clave de cada factura será 
#el número de factura y el valor el coste de la factura. El programa debe preguntar 
#al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
#Si desea añadir una nueva factura se preguntará por el número de factura y su coste
#y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número 
#de factura y se eliminará del diccionario. Después de cada operación el programa debe 
#mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

def pedirNumeroFactura():
    numero = input("Introduce el numero de factura: ")
    if str.isnumeric(numero):
        return numero
    else:
        raise TypeError
    
def pedirCoste():
    coste = input("Introduce el coste de la factura: ")
    try:
        coste = float(coste)
        return coste
    except:
        raise TypeError    
    
def aniadirFactura(facturas: dict, numero_factura, coste_factura):
    facturas[numero_factura] = coste_factura

def comprobarFactura(facturas, factura):
    if factura in facturas:
        return True
    else:
        return False

def pagar(facturas, numero_factura):
    if numero_factura not in facturas:
        raise KeyError
    del facturas[numero_factura]

if __name__ == '__main__':
    cantidad_cobrada = 0
    facturas = {}

    funcion = input("(1)Añadir factura\n(2)Pagar factura\n(3)Terminar\n> ")
    while funcion != "3":
        if funcion == "1":
            factura = pedirNumeroFactura()
            coste = pedirCoste()
            aniadirFactura(facturas, factura, coste)
            print(cantidad_cobrada)
        elif funcion == "2":
            factura = pedirNumeroFactura()
            if comprobarFactura(facturas, factura):
                cantidad_cobrada += facturas[factura]
                pagar(facturas, factura)
                print(cantidad_cobrada)
            else:
                print("La factura no existe")
        else:
            print("Entrada invalida")
        funcion = input("(1)Añadir factura\n(2)Pagar factura\n(3)Terminar\n> ")