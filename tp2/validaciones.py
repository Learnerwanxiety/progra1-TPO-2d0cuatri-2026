"""
Módulo encargado de solicitar y validar los datos ingresados por el
usuario durante la ejecución del programa.
"""

import consultas


def solicitar_codigo_valido(matriz):
    codigo_str = input("Ingrese el código del registro: ")
    while not (codigo_str.isdigit() and consultas.existe_codigo(matriz, int(codigo_str))):
        print("El código ingresado no existe. Intente nuevamente.")
        codigo_str = input("Ingrese el código del registro: ")
    return int(codigo_str)


def solicitar_genero_valido(generos_disponibles):
    print("\nGéneros disponibles:")
    indice = 0
    while indice < len(generos_disponibles):
        print(f"{indice + 1}. {generos_disponibles[indice]}")
        indice += 1

    opcion_str = input("Seleccione el número de género: ")
    while not (opcion_str.isdigit() and 1 <= int(opcion_str) <= len(generos_disponibles)):
        print("Opción inválida. Intente nuevamente.")
        opcion_str = input("Seleccione el número de género: ")

    return generos_disponibles[int(opcion_str) - 1]


def solicitar_texto_no_vacio(mensaje):
    texto = input(mensaje)
    while texto.strip() == "":
        print("Debe ingresar un texto válido.")
        texto = input(mensaje)
    return texto


def solicitar_cantidad_caracteres(longitud_maxima):
    mensaje = f"Ingrese la cantidad de caracteres a mostrar (1 a {longitud_maxima}): "
    cantidad_str = input(mensaje)
    while not (cantidad_str.isdigit() and 1 <= int(cantidad_str) <= longitud_maxima):
        print("Cantidad inválida.")
        cantidad_str = input(mensaje)
    return int(cantidad_str)
