def obtener_actividades():
    return ["Musculación", "Funcional", "Spinning", "Yoga", "Crossfit"]

def obtener_estados():
    return ["Activo", "Inactivo"]

def cargar_datos_iniciales():

    matriz = [
        [1, "Juan Perez", "Musculación", 15000.0, "Activo"],
        [2, "Ana Gomez", "Yoga", 12000.0, "Activo"],
        [3, "Pedro Lopez", "Spinning", 13500.0, "Inactivo"],
        [4, "Laura Diaz", "Crossfit", 18000.0, "Activo"],
        [5, "Marcos Ruiz", "Funcional", 14000.0, "Activo"],
    ]
    return matriz
