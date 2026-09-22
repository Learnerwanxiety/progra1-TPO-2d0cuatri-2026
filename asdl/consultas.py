"""
Módulo encargado de las búsquedas y filtros sobre la matriz de registros.
"""


def buscar_por_codigo(matriz, codigo):
    """
    Busca un registro en la matriz según su código, recorriendo la matriz
    de forma secuencial. Retorna el registro si lo encuentra, o None si
    no existe ningún registro con ese código.
    """
    encontrado = None
    i = 0
    while i < len(matriz) and encontrado is None:
        if matriz[i][0] == codigo:
            encontrado = matriz[i]
        i += 1
    return encontrado


def existe_codigo(matriz, codigo):
    """Indica si existe un registro con el código indicado en la matriz."""
    return buscar_por_codigo(matriz, codigo) is not None


def obtener_generos_disponibles(matriz):
    """
    Retorna una lista con los géneros distintos presentes en la matriz,
    sin repetidos, respetando el orden en que aparecen.
    """
    generos = []
    for registro in matriz:
        genero = registro[2]
        if genero not in generos:
            generos.append(genero)
    return generos


def filtrar_por_genero(matriz, genero):
    """Retorna una nueva matriz con los registros que pertenecen al género indicado."""
    matriz_filtrada = []
    for registro in matriz:
        if registro[2] == genero:
            matriz_filtrada.append(registro)
    return matriz_filtrada
