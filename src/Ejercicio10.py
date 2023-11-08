#Ejercicio 3.2.10¶
#Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
#Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
# y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, 
# correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. 
# El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, 
# (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, 
# (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

#    Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
#    Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
#    Preguntar por el NIF del cliente y mostrar sus datos.
#    Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
#    Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
#    Terminar el programa.

def pedirNif():
    nif = input("Introduce un NIF: ")
    return nif

def pedirNombre():
    nombre = input("Introduce un nombre: ")
    return nombre

def pedirDireccion():
    direccion = input("Introduce un direccion: ")
    return direccion

def pedirTelefono():
    telefono = input("Introduce un numero: ")
    return telefono

def pedirCorreo():
    correo = input("Introduce un correo: ")
    return correo

def pedirPreferente():
    preferente = input("Introduce si es preferente o no (s/n): ")
    if preferente == "s":
        return True
    else:
        return False
    
def pedirDatos():
    datos = []    
    nombre = pedirNombre()
    direccion = pedirDireccion()
    telefono = pedirTelefono()
    correo = pedirCorreo()
    preferente = pedirPreferente()
        
    datos.append({"nombre": nombre})
    datos.append({"direccion": direccion})
    datos.append({"telefono": telefono})
    datos.append({"correo": correo})
    datos.append({"preferente": preferente})
    return datos
    
def aniadirUsuario(lista_usuarios: dict, nif: str, datos: list):
    lista_usuarios[nif] = datos
    return lista_usuarios

def comprobarUsuario(lista_usuarios: dict, nif: str):
    if nif in lista_usuarios:
        return True
    else:
        return False

def eliminarCliente(lista_usuarios: dict, nif: str):
    del lista_usuarios[nif]
    return lista_usuarios

def buscarCliente(lista_usuarios: dict, nif: str):
    if nif in lista_usuarios:
        return f"{nif} {lista_usuarios[nif]}"
    
def imprimirUsuarios(lista_usuarios: dict):
    for usuario in lista_usuarios:
        print(f"{usuario} {lista_usuarios[usuario]}")

def usuariosPreferente(lista_usuarios):
    usuarios_preferentes = {}
    for usuario in lista_usuarios:
        if lista_usuarios[usuario][4]["preferente"] == True:
            usuarios_preferentes[usuario] = lista_usuarios[usuario]
    return usuarios_preferentes
        
def menu():
    
    usuarios = {}
    
    entrada = input("(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar\n> ")
    while entrada != "6":
        if entrada == "1":
            nif = pedirNif()
            if comprobarUsuario(usuarios, nif):
                print("El usuario ya existe.")
            else:
                datos = pedirDatos()
                aniadirUsuario(usuarios, nif, datos)    
        elif entrada == "2":
            nif = pedirNif()
            if comprobarUsuario(usuarios, nif):
                eliminarCliente(usuarios, nif)
            else:
                print("El usuario no existe.")
            
        elif entrada == "3":
            nif = pedirNif()
            if buscarCliente(usuarios, nif) == None:
                print("No existe este cliente")
            else:
                print(buscarCliente(usuarios, nif))
        
        elif entrada == "4":
            imprimirUsuarios(usuarios)
            
        elif entrada == "5":
            usuarios_preferentes = usuariosPreferente(usuarios)
            imprimirUsuarios(usuarios_preferentes)
            
        else:
            print("Entrada invalida.")        
        
        entrada = input("(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar\n> ")
        
if __name__ == '__main__':
    menu()
