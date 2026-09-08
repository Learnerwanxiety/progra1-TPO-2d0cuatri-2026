# datos.py
# Contiene los datos iniciales (hardcodeados) y las categorías definidas
# para la temática "Gestión de gimnasio".


def obtener_actividades():
    """Devuelve la lista de actividades válidas para los socios."""
    return ["Musculación", "Funcional", "Spinning", "Yoga", "Crossfit"]


def obtener_estados():
    """Devuelve la lista de estados válidos para los socios."""
    return ["Activo", "Inactivo"]


def cargar_datos_iniciales():
    """
    Crea y devuelve la matriz (lista de listas) con los registros
    iniciales del sistema. Cada fila representa un socio con el
    formato:
    [numero_socio, nombre, actividad_principal, valor_cuota, estado]
    """
    matriz = [
        [1, "Juan Perez", "Musculación", 15000.0, "Activo"],
        [2, "Ana Gomez", "Yoga", 12000.0, "Activo"],
        [3, "Pedro Lopez", "Spinning", 13500.0, "Inactivo"],
        [4, "Laura Diaz", "Crossfit", 18000.0, "Activo"],
        [5, "Marcos Ruiz", "Funcional", 14000.0, "Activo"],
    ]
    return matriz
