"""
Módulo encargado de la presentación tabular de los registros.
"""


def abreviar_texto(texto, longitud_maxima):
    """
    Recorta un texto a la longitud máxima indicada, agregando puntos
    suspensivos cuando corresponde, para conservar la alineación de
    las columnas en la tabla.
    """
    if len(texto) > longitud_maxima:
        resultado = texto[:longitud_maxima - 3] + "..."
    else:
        resultado = texto
    return resultado


def mostrar_tabla(matriz):
    """Muestra los registros de la matriz en formato de tabla, alineada y con encabezados."""
    encabezado = f"{'Código':<8}{'Título':<26}{'Género':<17}{'Puntuación':<12}{'Reseña':<50}"
    print(encabezado)
    print("-" * len(encabezado))
    for registro in matriz:
        codigo = registro[0]
        titulo = registro[1]
        genero = registro[2]
        puntuacion = registro[3]
        resena_abreviada = abreviar_texto(registro[4], 47)
        fila = f"{codigo:<8}{titulo:<26}{genero:<17}{puntuacion:<12}{resena_abreviada:<50}"
        print(fila)
