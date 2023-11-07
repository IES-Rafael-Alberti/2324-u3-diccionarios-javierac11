#Ejercicio 3.2.5¶
#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
#{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada 
#asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las 
#asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

def generaMensajes(creditos_asignaturas: dict):
    mensajes = []
    for credito_asignatura in creditos_asignaturas:
        mensaje = f"{credito_asignatura} tiene {creditos_asignaturas[credito_asignatura]}"
        mensajes.append(mensaje)
    return mensajes

if __name__ == '__main__':
    creditos = {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}
    mensajes = generaMensajes(creditos)
    for mensaje in mensajes:
        print(mensaje)
    