def quitar_espacios(texto):
    inicio = 0
    while inicio < len(texto) and (texto[inicio] == " " or texto[inicio] == "\t" or texto[inicio] == "\n"):
        inicio += 1

    fin = len(texto) - 1
    while fin >= inicio and (texto[fin] == " " or texto[fin] == "\t" or texto[fin] == "\n"):
        fin -= 1

    resultado = ""
    for i in range(inicio, fin + 1):
        resultado += texto[i]
    return resultado


def son_digitos(texto):
    if len(texto) == 0:
        return False
    digitos = "0123456789"
    for caracter in texto:
        if caracter not in digitos:
            return False
    return True


def es_entero(texto):
    texto = quitar_espacios(texto)
    if texto == "":
        return False

    inicio = 0
    if texto[0] == "-":
        inicio = 1

    if inicio >= len(texto):
        return False

    sin_signo = ""
    for i in range(inicio, len(texto)):
        sin_signo += texto[i]

    return son_digitos(sin_signo)


def es_decimal(texto):
    texto = quitar_espacios(texto)
    if texto == "":
        return False

    inicio = 0
    if texto[0] == "-":
        inicio = 1

    if inicio >= len(texto):
        return False

    sin_signo = ""
    for i in range(inicio, len(texto)):
        sin_signo += texto[i]
    contador_puntos = 0
    parte_entera = ""
    parte_decimal = ""

    for caracter in sin_signo:
        if caracter == ".":
            contador_puntos += 1
        elif contador_puntos == 0:
            parte_entera += caracter
        elif contador_puntos == 1:
            parte_decimal += caracter

    if contador_puntos == 0:
        return parte_entera != "" and son_digitos(parte_entera)
    if contador_puntos == 1:
        return parte_entera != "" and parte_decimal != "" and son_digitos(parte_entera) and son_digitos(parte_decimal)
    return False


def opcion_valida(opcion, minimo, maximo):
    if not es_entero(opcion):
        return False
    numero = int(opcion)
    return minimo <= numero <= maximo


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
    while quitar_espacios(texto) == "":
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
