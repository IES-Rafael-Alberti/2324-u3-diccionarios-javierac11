#Ejercicio 3.2.1¶
#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
#pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

def devuelveSimbolo(divisa: str, divisas: dict):
    if divisa in divisas:
        simbolo = divisas[divisa]
        return simbolo
    else:
        raise IndexError


        
if __name__ == '__main__':
    try:
        divisas = {"Euro": "€", "Dollar": "$", 'Yen': '¥'}
        divisa = input("Introduce una divisa: ")
        print(devuelveSimbolo(divisa, divisas))
    except:
        print("ERROR")