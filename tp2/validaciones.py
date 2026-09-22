def opcion_valida(opcion):
    # Valida que la opcion del menu sea un numero entero entre 0 y 8
    if opcion.isdigit() and int(opcion) >= 0 and int(opcion) <= 8:
        return True
    else:
        return False


def es_numero(texto):
    # Valida que el texto ingresado sea numerico (sirve para codigos y cantidades)
    return texto.isdigit()


def categoria_valida(categoria, cantidad_categorias):
    # Valida que la opcion de categoria elegida este dentro del rango disponible
    if categoria.isdigit() and int(categoria) >= 1 and int(categoria) <= cantidad_categorias:
        return True
    else:
        return False


def palabra_valida(palabra):
    # Valida que se haya ingresado algo (no vacio ni solo espacios) para buscar
    if palabra.strip() == "":
        return False
    else:
        return True
