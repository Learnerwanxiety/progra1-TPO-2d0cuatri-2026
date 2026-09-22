"""
Módulo encargado del procesamiento estadístico de la matriz de registros.
Cada cálculo se resuelve en una función específica e independiente de
la presentación de resultados.
"""


def contar_registros(matriz):
    """Retorna la cantidad total de registros de la matriz."""
    return len(matriz)


def contar_por_genero(matriz, genero):
    """Retorna la cantidad de registros que pertenecen al género indicado."""
    contador = 0
    for registro in matriz:
        if registro[2] == genero:
            contador += 1
    return contador


def promedio_puntuacion(matriz):
    """
    Calcula el promedio de puntuación de todos los registros.
    La puntuación se almacena como cadena, por lo que se convierte
    a entero antes de sumarla.
    """
    suma = 0
    for registro in matriz:
        suma += int(registro[3])
    return suma / len(matriz)


def promedio_longitud_texto(matriz):
    """Calcula la longitud promedio (en caracteres) de las reseñas de todos los registros."""
    suma_longitudes = 0
    for registro in matriz:
        suma_longitudes += len(registro[4])
    return suma_longitudes / len(matriz)


def registro_texto_mas_largo(matriz):
    """Retorna el registro completo cuya reseña tiene la mayor longitud."""
    registro_mas_largo = matriz[0]
    for registro in matriz:
        if len(registro[4]) > len(registro_mas_largo[4]):
            registro_mas_largo = registro
    return registro_mas_largo
