#Ejercicio 3.2.6¶
#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
#(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
#Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

def pedirNombre():
    nombre = input("Introduce un nombre: ")
    return nombre

def pedirEdad():
    edad = int(input("Introduce un edad: "))
    return edad

def pedirSexo():
    sexo = input("Introduce un sexo: ")
    return sexo

def pedirTelefono():
    telefono = input("Introduce un numero: ")
    return telefono

def pedirCorreo():
    correo = input("Introduce un correo: ")
    return correo

def pedirCliente():
    cliente = {}
    nombre = pedirNombre()
    cliente["nombre"] = nombre
    print(cliente) 
#    edad, sexo, teléfono, correo electrónico
    edad = pedirEdad()
    cliente["edad"] = edad
    print(cliente)
    sexo = pedirSexo()
    cliente["sexo"] = sexo
    print(cliente)
    telefono = pedirTelefono()
    cliente["telefono"] = telefono
    print(cliente)
    correo = pedirCorreo()
    cliente["correo"] = correo
    print(cliente)
    return cliente

if __name__ == '__main__':
    pedirCliente()
    
    