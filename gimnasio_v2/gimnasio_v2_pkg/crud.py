import validaciones


def buscar_indice_por_numero(matriz, numero):
    for i in range(len(matriz)):
        if matriz[i][0] == numero:
            return i
    return -1


def alta_socio(matriz, actividades, estados):

    print("\n--- Alta de socio ---")

    numero = validaciones.pedir_entero("Ingrese número de socio: ")
    while validaciones.numero_socio_repetido(matriz, numero):
        print("Ya existe un socio con ese número.")
        numero = validaciones.pedir_entero("Ingrese número de socio: ")

    nombre = validaciones.pedir_texto_no_vacio("Ingrese nombre del socio: ")
    actividad = validaciones.elegir_categoria(actividades, "Seleccione la actividad principal:")
    cuota = validaciones.pedir_decimal("Ingrese valor de la cuota: ")
    estado = validaciones.elegir_categoria(estados, "Seleccione el estado del socio:")

    nuevo_socio = [numero, nombre, actividad, cuota, estado]
    matriz.append(nuevo_socio)
    print("Socio agregado correctamente.")


def consultar_socio(matriz):
    print("\n--- Consulta de socio ---")
    numero = validaciones.pedir_entero("Ingrese el número de socio a consultar: ")
    indice = buscar_indice_por_numero(matriz, numero)

    if indice == -1:
        print("No se encontró ningún socio con ese número.")
        return

    socio = matriz[indice]
    print("Número de socio:", socio[0])
    print("Nombre:", socio[1])
    print("Actividad principal:", socio[2])
    print("Valor de cuota:", socio[3])
    print("Estado:", socio[4])


def modificar_socio(matriz, actividades, estados):
    print("\n--- Modificación de socio ---")
    numero = validaciones.pedir_entero("Ingrese el número de socio a modificar: ")
    indice = buscar_indice_por_numero(matriz, numero)

    if indice == -1:
        print("No se encontró ningún socio con ese número.")
        return

    print("Socio encontrado:", matriz[indice])
    print("¿Qué dato desea modificar?")
    print("1. Nombre")
    print("2. Actividad principal")
    print("3. Valor de cuota")
    print("4. Estado")
    opcion_texto = input("Ingrese una opción: ")
    while not validaciones.opcion_valida(opcion_texto, 1, 4):
        print("Opción inválida.")
        opcion_texto = input("Ingrese una opción: ")
    opcion = int(opcion_texto)

    if opcion == 1:
        matriz[indice][1] = validaciones.pedir_texto_no_vacio("Ingrese el nuevo nombre: ")
    elif opcion == 2:
        matriz[indice][2] = validaciones.elegir_categoria(actividades, "Seleccione la nueva actividad:")
    elif opcion == 3:
        matriz[indice][3] = validaciones.pedir_decimal("Ingrese el nuevo valor de cuota: ")
    elif opcion == 4:
        matriz[indice][4] = validaciones.elegir_categoria(estados, "Seleccione el nuevo estado:")

    print("Socio modificado correctamente.")


def eliminar_socio(matriz):
    print("\n--- Eliminación de socio ---")
    numero = validaciones.pedir_entero("Ingrese el número de socio a eliminar: ")
    indice = buscar_indice_por_numero(matriz, numero)

    if indice == -1:
        print("No se encontró ningún socio con ese número.")
        return

    print("Socio a eliminar:", matriz[indice])
    confirmacion = input("¿Confirma la eliminación? (s/n): ")
    if confirmacion.lower() == "s":
        matriz.pop(indice)
        print("Socio eliminado correctamente.")
    else:
        print("Operación cancelada.")


def completar_texto(texto, ancho):
    texto = str(texto)
    if len(texto) > ancho:
        resultado = ""
        for i in range(ancho):
            resultado += texto[i]
        return resultado
    return texto + " " * (ancho - len(texto))


def mostrar_socios(matriz, ancho_descripcion):

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
def consultar_por_actividad(matriz, actividades):

    actividad = validaciones.elegir_categoria(actividades, "Seleccione la actividad a consultar:")
    encontrados = []
    for socio in matriz:
        if socio[2] == actividad:
            encontrados.append(socio)

    if len(encontrados) == 0:
        print("No hay socios registrados en esa actividad.")
    else:
        mostrar_socios(encontrados, 12)
