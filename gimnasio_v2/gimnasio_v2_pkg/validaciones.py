def es_entero(texto):
    texto = texto.strip()
    if texto == "":
        return False
    if texto[0] == "-":
        texto = texto[1:]
    if texto == "":
        return False
    return texto.isdigit()

def es_decimal(texto):
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
    if not es_entero(opcion):
        return False
    numero = int(opcion)
    return minimo <= numero <= maximo
    #Evalúa si numero es mayor o igual que minimo y menor
    # o igual que maximo. Retorna True si está dentro del rango o False si está fuera.


def numero_socio_repetido(matriz, numero):
    for fila in matriz:
        if fila[0] == numero:
            return True
    return False


def actividad_valida(actividad, actividades):
    for a in actividades:
        if a.lower() == actividad.lower():
            return True
    return False


def estado_valido(estado, estados):

    for e in estados:
        if e.lower() == estado.lower():
            return True
    return False


def pedir_entero(mensaje):
    texto = input(mensaje)
    while not es_entero(texto):
        print("Debe ingresar un número entero válido.")
        texto = input(mensaje)
    return int(texto)


def pedir_decimal(mensaje):
    texto = input(mensaje)
    while not es_decimal(texto):
        print("Debe ingresar un valor numérico válido.")
        texto = input(mensaje)
    return float(texto)


def pedir_texto_no_vacio(mensaje):
    texto = input(mensaje)
    while texto.strip() == "":
        print("El dato no puede estar vacío.")
        texto = input(mensaje)
    return texto


def elegir_categoria(categorias, mensaje):

    print(mensaje)
    for i in range(len(categorias)):
        print(str(i + 1) + ". " + categorias[i])
    opcion = input("Ingrese el número de opción: ")
    while not opcion_valida(opcion, 1, len(categorias)):
        print("Opción inválida.")
        opcion = input("Ingrese el número de opción: ")
    return categorias[int(opcion) - 1]
