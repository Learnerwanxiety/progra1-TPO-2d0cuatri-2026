def completar_texto(texto, ancho):
    """
    Recibe un texto y un ancho determinado.
    Devuelve el texto completado con espacios a la derecha
    hasta alcanzar ese ancho. Si el texto ya es más largo
    que el ancho, se corta para no romper la alineación.
    """
    texto = str(texto)
    if len(texto) > ancho:
        return texto[:ancho]
    return texto + " " * (ancho - len(texto))


def mostrar_matriz(matriz, ancho_descripcion=12):
    """
    Muestra la matriz en formato tabular.
    Todas las columnas se alinean usando completar_texto(),
    con la de descripción usando un ancho fijo definido aparte.
    """
    encabezado = (
        completar_texto("ID", 4)
        + completar_texto("Nombre", 15)
        + completar_texto("Descripción", ancho_descripcion)
        + completar_texto("Precio", 10)
        + completar_texto("Estado", 10)
    )
    print(encabezado)
    print("-" * len(encabezado))

    for fila in matriz:
        id_, nombre, descripcion, precio, estado = fila
        linea = (
            completar_texto(id_, 4)
            + completar_texto(nombre, 15)
            + completar_texto(descripcion, ancho_descripcion)
            + completar_texto(precio, 10)
            + completar_texto(estado, 10)
        )
        print(linea)
matriz = [
[1, "Juan Perez", "Musculación", 15000.0, "Activo"],
[2, "Ana Gomez", "Yoga", 12000.0, "Activo"],
[3, "Pedro Lopez", "Spinning", 13500.0, "Inactivo"],
[4, "Laura Diaz", "Crossfit", 18000.0, "Activo"],
[5, "Marcos Ruiz", "Funcional", 14000.0, "Activo"],
]
mostrar_matriz(matriz, 12)