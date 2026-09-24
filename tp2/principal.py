"""
Módulo principal del sistema de Reseñas de películas y series.
"""

import datos
import consultas
import cadenas
import estadisticas
import validaciones
import presentacion
import menu


def procesar_mostrar_todos(matriz):
    presentacion.mostrar_tabla(matriz)


def procesar_consulta_codigo(matriz):
    codigo = validaciones.solicitar_codigo_valido(matriz)
    registro = consultas.buscar_por_codigo(matriz, codigo)
    presentacion.mostrar_registro_completo(registro)


def procesar_vista_previa(matriz):
    codigo = validaciones.solicitar_codigo_valido(matriz)
    registro = consultas.buscar_por_codigo(matriz, codigo)
    resena = registro[4]

    cantidad = validaciones.solicitar_cantidad_caracteres(len(resena))
    inicio, final = cadenas.obtener_vista_previa(resena, cantidad)

    print(f"\nTexto completo: {resena}")
    print(f"Primeros {cantidad} caracteres: {inicio}")
    print(f"Últimos {cantidad} caracteres: {final}")


def procesar_normalizar_texto(matriz):
    codigo = validaciones.solicitar_codigo_valido(matriz)
    registro = consultas.buscar_por_codigo(matriz, codigo)
    resena_original = registro[4]

    resena_sin_espacios = cadenas.eliminar_espacios_extremos(resena_original)
    resena_normalizada = cadenas.normalizar_texto_a_minusculas(resena_sin_espacios)

    palabra_original = validaciones.solicitar_texto_no_vacio("Ingrese la palabra o expresión a reemplazar: ")
    palabra_nueva = validaciones.solicitar_texto_no_vacio("Ingrese el nuevo contenido: ")
    resena_transformada = cadenas.reemplazar_palabra(resena_normalizada, palabra_original.lower(), palabra_nueva)

    print(f"\nTexto original: {resena_original}")
    print(f"Texto transformado: {resena_transformada}")


def procesar_consulta_por_palabra(matriz):
    palabra = validaciones.solicitar_texto_no_vacio("Ingrese la palabra o expresión a buscar: ")
    matriz_filtrada = consultas.filtrar_por_palabra(matriz, palabra)

    if len(matriz_filtrada) > 0:
        print(f"\nSe encontraron {len(matriz_filtrada)} registro(s) con la palabra '{palabra}':")
        presentacion.mostrar_tabla(matriz_filtrada)
        total_apariciones = consultas.contar_apariciones_totales(matriz_filtrada, palabra)
        print(f"Cantidad total de apariciones: {total_apariciones}")
    else:
        print(f"\nNo se encontraron registros que contengan la palabra '{palabra}'.")


def procesar_separacion_texto(matriz):
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
    generos_disponibles = consultas.obtener_generos_disponibles(matriz)
    genero_elegido = validaciones.solicitar_genero_valido(generos_disponibles)
    matriz_filtrada = consultas.filtrar_por_genero(matriz, genero_elegido)

    if len(matriz_filtrada) > 0:
        print(f"\nRegistros del género '{genero_elegido}':")
        presentacion.mostrar_tabla(matriz_filtrada)
    else:
        print(f"\nNo existen registros del género '{genero_elegido}'.")


def procesar_estadisticas(matriz):
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
    matriz = datos.obtener_registros()
    opcion = -1
    while opcion != 0:
        menu.mostrar_menu()
        opcion_str = input("Seleccione una opción: ")
        while not (opcion_str.isdigit() and opcion_str in ("0", "1", "2", "3", "4", "5", "6", "7", "8")):
            print("Opción inválida. Intente nuevamente.")
            opcion_str = input("Seleccione una opción: ")
        opcion = int(opcion_str)

        if opcion == 1:
            procesar_mostrar_todos(matriz)
        elif opcion == 2:
            procesar_consulta_codigo(matriz)
        elif opcion == 3:
            procesar_vista_previa(matriz)
        elif opcion == 4:
            procesar_normalizar_texto(matriz)
        elif opcion == 5:
            procesar_consulta_por_palabra(matriz)
        elif opcion == 6:
            procesar_separacion_texto(matriz)
        elif opcion == 7:
            procesar_consulta_por_categoria(matriz)
        elif opcion == 8:
            procesar_estadisticas(matriz)


ejecutar_programa()
