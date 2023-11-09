#Ejercicio 3.2.4¶
#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato 
#dd de <mes> de aaaa donde <mes> es el nombre del mes.

def leeFecha():
    fecha = input("Introduce una fecha con el formato dd/mm/aaaa: ")
    fecha_separada = fecha.split("/")
    if len(fecha_separada) != 3:
        raise ValueError
    for numeros in fecha_separada:
        if not str.isnumeric(numeros):
            raise TypeError
    if int(fecha_separada[0]) < 1 or int(fecha_separada[0]) > 31:
        raise ValueError
    elif int(fecha_separada[1]) < 1 or int(fecha_separada[1]) > 12:
        raise ValueError
    return fecha

def generaMensaje(fecha):
    fecha_separada = fecha.split("/")
    meses = {
        "01": "Enero",
        "02": "Febrero",
        "03": "Marzo",
        "04": "Abril",
        "05": "Mayo",
        "06": "Junio",
        "07": "Julio",
        "08": "Agosto",
        "09": "Septiembre",
        "10": "Octubre",
        "11": "Noviembre",
        "12": "Diciembre"
    }
    mensaje = fecha_separada[0] + " de " + meses[fecha_separada[1]] + " de " + fecha_separada[2]
    return mensaje

if __name__ == '__main__':
    fecha = leeFecha()
    print(generaMensaje(fecha))
    