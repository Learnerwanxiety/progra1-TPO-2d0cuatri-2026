# validaciones.py
# Funciones encargadas de validar los datos ingresados por el usuario.


def es_entero(texto):
    """Verifica si un texto representa un número entero (positivo o negativo)."""
    texto = texto.strip()
    if texto == "":
        return False
    if texto[0] == "-":
        texto = texto[1:]
    if texto == "":
        return False
    return texto.isdigit()


def es_decimal(texto):
    """Verifica si un texto representa un número decimal (positivo o negativo)."""
    texto = texto.strip()
    if texto == "":
        return False
    if texto[0] == "-":
        texto = texto[1:]
    partes = texto.split(".")
    if len(partes) == 1:
        return partes[0] != "" and partes[0].isdigit()
    if len(partes) == 2:
        return partes[0].isdigit() and partes[1].isdigit() and partes[0] != "" and partes[1] != ""
    return False


def opcion_valida(opcion, minimo, maximo):
    """Verifica que la opción ingresada sea un entero dentro de un rango."""
    if not es_entero(opcion):
        return False
    numero = int(opcion)
    return minimo <= numero <= maximo


def numero_socio_repetido(matriz, numero):
    """Verifica si ya existe un socio con el número indicado."""
    for fila in matriz:
        if fila[0] == numero:
            return True
    return False


def actividad_valida(actividad, actividades):
    """Verifica si una actividad pertenece a la lista de categorías definidas."""
    for a in actividades:
        if a.lower() == actividad.lower():
            return True
    return False


def estado_valido(estado, estados):
    """Verifica si un estado pertenece a la lista de estados definidos."""
    for e in estados:
        if e.lower() == estado.lower():
            return True
    return False


def pedir_entero(mensaje):
    """Pide un número entero por teclado hasta que sea válido."""
    texto = input(mensaje)
    while not es_entero(texto):
        print("Debe ingresar un número entero válido.")
        texto = input(mensaje)
    return int(texto)


def pedir_decimal(mensaje):
    """Pide un número decimal por teclado hasta que sea válido."""
    texto = input(mensaje)
    while not es_decimal(texto):
        print("Debe ingresar un valor numérico válido.")
        texto = input(mensaje)
    return float(texto)


def pedir_texto_no_vacio(mensaje):
    """Pide un texto por teclado que no puede estar vacío."""
    texto = input(mensaje)
    while texto.strip() == "":
        print("El dato no puede estar vacío.")
        texto = input(mensaje)
    return texto


def elegir_categoria(categorias, mensaje):
    """
    Muestra una lista de categorías numeradas y devuelve la elegida
    por el usuario, validando que la opción sea correcta.
    """
    print(mensaje)
    for i in range(len(categorias)):
        print(str(i + 1) + ". " + categorias[i])
    opcion = input("Ingrese el número de opción: ")
    while not opcion_valida(opcion, 1, len(categorias)):
        print("Opción inválida.")
        opcion = input("Ingrese el número de opción: ")
    return categorias[int(opcion) - 1]
