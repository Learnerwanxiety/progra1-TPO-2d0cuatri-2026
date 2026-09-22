"""
Módulo encargado del procesamiento de cadenas sobre el texto principal
(la Reseña) de un registro.
"""


def separar_en_palabras(texto):
    """Separa un texto en una lista de palabras, usando el espacio como separador."""
    return texto.split()


def reconstruir_texto(lista_palabras, separador):
    """
    Reconstruye una cadena a partir de una lista de palabras, uniéndolas
    con el separador indicado.
    """
    return separador.join(lista_palabras)
