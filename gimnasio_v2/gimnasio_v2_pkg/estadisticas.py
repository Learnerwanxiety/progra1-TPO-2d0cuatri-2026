import validaciones


def cantidad_total(matriz):

    return len(matriz)


def cantidad_por_actividad(matriz, actividad):

    contador = 0
    for socio in matriz:
        if socio[2] == actividad:
            contador += 1
    return contador


def cantidad_por_estado(matriz, estado):

    contador = 0
    for socio in matriz:
        if socio[4] == estado:
            contador += 1
    return contador


def cuota_promedio(matriz):

    if len(matriz) == 0:
        return 0
    total = 0
    for socio in matriz:
        total += socio[3]
    return total / len(matriz)


def actividad_mas_popular(matriz, actividades):
    max_cantidad = -1
    actividad_top = ""
    for actividad in actividades:
        cantidad = cantidad_por_actividad(matriz, actividad)
        if cantidad > max_cantidad:
            max_cantidad = cantidad
            actividad_top = actividad
    return actividad_top, max_cantidad


def mostrar_estadisticas(matriz, actividades):
    print("\n--- Estadísticas del gimnasio ---")
    print("Cantidad total de socios:", cantidad_total(matriz))

    actividad = validaciones.elegir_categoria(
        actividades, "Seleccione una actividad para ver su cantidad de socios:")
    print("Cantidad de socios en", actividad + ":", cantidad_por_actividad(matriz, actividad))

    print("Cantidad de socios activos:", cantidad_por_estado(matriz, "Activo"))
    print("Cantidad de socios inactivos:", cantidad_por_estado(matriz, "Inactivo"))
    print("Valor promedio de cuota: $" + str(round(cuota_promedio(matriz), 2)))

    top, cantidad_top = actividad_mas_popular(matriz, actividades)
    print("Actividad más popular:", top, "con", cantidad_top, "socios")
