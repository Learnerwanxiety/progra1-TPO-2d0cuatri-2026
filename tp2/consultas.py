"""
Módulo encargado de las búsquedas y filtros sobre la matriz de registros.
"""


def buscar_por_codigo(matriz, codigo):
    encontrado = None
    i = 0
    while i < len(matriz) and encontrado is None:
        if matriz[i][0] == codigo:
            encontrado = matriz[i]
        i += 1
    return encontrado


def existe_codigo(matriz, codigo):
    return buscar_por_codigo(matriz, codigo) is not None


def obtener_generos_disponibles(matriz):
    generos = []
    for registro in matriz:
        genero = registro[2]
        if genero not in generos:
            generos.append(genero)
    return generos


def filtrar_por_genero(matriz, genero):
    matriz_filtrada = []
    for registro in matriz:
        if registro[2] == genero:
            matriz_filtrada.append(registro)
    return matriz_filtrada
