"""
Módulo encargado del procesamiento de cadenas sobre el texto principal
(la Reseña) de un registro.
"""


def separar_en_palabras(texto):
    return texto.split()


def reconstruir_texto(lista_palabras, separador):
    return separador.join(lista_palabras)


def capitalizar_texto(texto):
    return texto.capitalize()


def normalizar_texto_a_minusculas(texto):
    return texto.lower()
