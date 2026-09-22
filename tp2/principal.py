"""
Módulo principal del sistema de Reseñas de películas y series.
Contiene esta entrega: funcionalidades 6 (Separar y reconstruir un
texto), 7 (Consultar registros por categoría) y 8 (Procesamiento
estadístico).
"""

import datos
import consultas
import cadenas
import estadisticas
import validaciones
import presentacion
import menu


def procesar_separacion_texto(matriz):
    """Funcionalidad 6: separa en palabras la reseña de un registro y la reconstruye."""
    codigo = validaciones.solicitar_codigo_valido(matriz)
    registro = consultas.buscar_por_codigo(matriz, codigo)
    resena = registro[4]
    palabras = cadenas.separar_en_palabras(resena)

    print(f"\nTexto original: {resena}")
    print(f"Cantidad de palabras: {len(palabras)}")
    print("Palabras obtenidas:")
    for palabra in palabras:
        print(f"- {palabra}")

    separador = input("Ingrese el separador para reconstruir el texto (por ejemplo, '-'): ")
    texto_reconstruido = cadenas.reconstruir_texto(palabras, separador)
    print(f"Texto reconstruido: {texto_reconstruido}")


def procesar_consulta_por_categoria(matriz):
    """Funcionalidad 7: filtra y muestra los registros del género elegido por el usuario."""
    generos_disponibles = consultas.obtener_generos_disponibles(matriz)
    genero_elegido = validaciones.solicitar_genero_valido(generos_disponibles)
    matriz_filtrada = consultas.filtrar_por_genero(matriz, genero_elegido)

    if len(matriz_filtrada) > 0:
        print(f"\nRegistros del género '{genero_elegido}':")
        presentacion.mostrar_tabla(matriz_filtrada)
    else:
        print(f"\nNo existen registros del género '{genero_elegido}'.")


def procesar_estadisticas(matriz):
    """Funcionalidad 8."""
    total = estadisticas.contar_registros(matriz)
    print(f"\nCantidad total de registros: {total}")

    generos_disponibles = consultas.obtener_generos_disponibles(matriz)
    genero_elegido = validaciones.solicitar_genero_valido(generos_disponibles)
    cantidad_genero = estadisticas.contar_por_genero(matriz, genero_elegido)
    print(f"Cantidad de registros del género '{genero_elegido}': {cantidad_genero}")

    promedio_punt = estadisticas.promedio_puntuacion(matriz)
    print(f"Promedio de puntuación: {promedio_punt:.2f}")

    promedio_long = estadisticas.promedio_longitud_texto(matriz)
    print(f"Longitud promedio de las reseñas: {promedio_long:.2f} caracteres")

    registro_largo = estadisticas.registro_texto_mas_largo(matriz)
    print(f"Registro con la reseña más larga: [{registro_largo[0]}] {registro_largo[1]}")


def ejecutar_programa():
    """Muestra el menú y ejecuta la opción elegida hasta que el usuario decida salir."""
    matriz = datos.obtener_registros()
    opcion = -1
    while opcion != 0:
        menu.mostrar_menu()
        opcion_str = input("Seleccione una opción: ")
        while not (opcion_str.isdigit() and opcion_str in ("0", "1", "2", "3")):
            print("Opción inválida. Intente nuevamente.")
            opcion_str = input("Seleccione una opción: ")
        opcion = int(opcion_str)

        if opcion == 1:
            procesar_separacion_texto(matriz)
        elif opcion == 2:
            procesar_consulta_por_categoria(matriz)
        elif opcion == 3:
            procesar_estadisticas(matriz)


ejecutar_programa()
