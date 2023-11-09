#Ejercicio 3.2.8¶
#Escribir un programa que cree un diccionario de traducción español-inglés. 
#El usuario introducirá las palabras en español e inglés separadas por dos puntos, 
#y cada par <palabra>:<traducción> separados por comas. El programa debe crear un 
#diccionario con las palabras y sus traducciones. Después pedirá una frase en español 
#y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está
#en el diccionario debe dejarla sin traducir

def leePalabrasTraducciones():
    palabras_traducciones = input("Introduce palabras y traducciones con el formato <palabra>:<traducción> y separados por \",\" ")
    palabras_traducciones_separadas = palabras_traducciones.split(",")
    for palabra_traduccion in palabras_traducciones_separadas:
        if len(palabra_traduccion.split(":")) != 2:
            raise ValueError
    return palabras_traducciones_separadas

def generaDiccionario(palabras_traducciones):
    diccionario = {}
    for palabra in palabras_traducciones:
        palabra_separada = palabra.split(":")
        diccionario[palabra_separada[0]] = palabra_separada[1]
    return diccionario

def traduceFrase(frase, diccionario):
    frase_separada = frase.split(" ")
    frase_traducida = ""
    for palabra in frase_separada:
        if palabra in diccionario:
            frase_traducida += f"{diccionario[palabra]} "
        else:
            frase_traducida += f"{palabra} "
    return frase_traducida

if __name__ == '__main__':
    
    palabras = leePalabrasTraducciones()
    diccionario = generaDiccionario(palabras)
    frase = input("Introduce una frase ")
    print(traduceFrase(frase, diccionario))