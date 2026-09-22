import datos
import validaciones
import cadenas
""" MOSTRAR DATOS """
ANCHO_CODIGO = 8
ANCHO_NOMBRE = 24
ANCHO_TEMA = 18
ANCHO_PUNTUACION = 12
ANCHO_DESCRIPCION = 35


def mostrar_registros(matriz_peliculas):
    print("-" * 100)
    print(f"{'CODIGO':<{ANCHO_CODIGO}} {'NOMBRE':<{ANCHO_NOMBRE}} {'TEMA':<{ANCHO_TEMA}} {'PUNTUACION':<{ANCHO_PUNTUACION}} {'DESCRIPCION':<{ANCHO_DESCRIPCION}}")
    print("-" * 100)
    for i in range(len(matriz_peliculas)):
        codigo = matriz_peliculas[i][0]
        nombre = matriz_peliculas[i][1]
        tema = matriz_peliculas[i][2]
        puntuacion = matriz_peliculas[i][3]
        descripcion = cadenas.abreviar_texto(matriz_peliculas[i][4], ANCHO_DESCRIPCION)
        print(f"{codigo:<{ANCHO_CODIGO}} {nombre:<{ANCHO_NOMBRE}} {tema:<{ANCHO_TEMA}} {puntuacion:<{ANCHO_PUNTUACION}} {descripcion:<{ANCHO_DESCRIPCION}}")
    print("-" * 100)


""" BUSQUEDA (reutilizable por consulta y vista previa) """
def buscar_registro(matriz_peliculas, codigo):
    # Recorre la matriz y devuelve el REGISTRO encontrado (la fila completa), o None si no existe
    registro_encontrado = None
    for i in range(len(matriz_peliculas)):
        if matriz_peliculas[i][0] == codigo:
            registro_encontrado = matriz_peliculas[i]
    return registro_encontrado


def pedir_codigo():
    # Pide un codigo por teclado y valida que sea numerico (no vacio, no letras)
    codigo_texto = input("Ingrese el codigo: ")
    while validaciones.es_numero(codigo_texto) == False:
        print("El codigo debe ser un numero")
        codigo_texto = input("Ingrese el codigo: ")
    return int(codigo_texto)


""" CONSULTAR REGISTRO (punto 2) """
def busqueda_codigo(matriz_peliculas):
    codigo = pedir_codigo()
    registro = buscar_registro(matriz_peliculas, codigo)

    if registro is None:
        print("Codigo no encontrado")
    else:
        print("-" * 40)
        print("Codigo:", registro[0])
        print("Nombre:", registro[1])
        print("Tema:", registro[2])
        print("Puntuacion:", registro[3])
        print("Reseña:", registro[4])
        print("-" * 40)


""" VISTA PREVIA DEL TEXTO (punto 3) """
def generar_vista_previa(matriz_peliculas):
    codigo = pedir_codigo()
    registro = buscar_registro(matriz_peliculas, codigo)

    if registro is None:
        print("Codigo no encontrado")
    else:
        reseña = registro[4]

        cantidad_texto = input("Cuantos caracteres desea ver del inicio y del final: ")
        while validaciones.es_numero(cantidad_texto) == False:
            print("Debe ingresar un numero")
            cantidad_texto = input("Cuantos caracteres desea ver del inicio y del final: ")
        cantidad = int(cantidad_texto)

        # Extraccion con indices y slicing, tal como pide la consigna
        inicio = reseña[:cantidad]     # primeros "cantidad" caracteres
        final = reseña[-cantidad:]     # ultimos "cantidad" caracteres

        print("-" * 40)
        print("Texto completo:", reseña)
        print(f"Primeros {cantidad} caracteres:", inicio)
        print(f"Ultimos {cantidad} caracteres:", final)
        print("-" * 40)
