#Ejercicio 3.2.2¶
#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de 
# teléfono es <teléfono>.

def pedirNombre():
    nombre = input("Introduce un nombre: ")
    return nombre

def pedirDireccion():
    direccion = input("Introduce un direccion: ")
    return direccion

def pedirTelefono():
    telefono = input("Introduce un numero: ")
    return telefono

def pedirEdad(): 
    edad = input("Introduce una edad: ")
    if str.isnumeric(edad):
        edad = int(edad)
        return edad
    else:
        raise ValueError    

def leeDatos():
    nombre = pedirNombre()
    direccion = pedirDireccion()
    telefono = pedirTelefono()
    edad = pedirEdad()
    datos = {"nombre": nombre, "direccion": direccion, "telefono": telefono, "edad": edad}
    return datos
    
def generaMensaje(datos: dict):
    return datos["nombre"] + " tiene "+ str(datos["edad"]) + " años, vive en " + datos["direccion"] + " y su número de teléfono es " + datos["telefono"]

if __name__ == '__main__':
    datos = leeDatos()
    print(generaMensaje(datos))