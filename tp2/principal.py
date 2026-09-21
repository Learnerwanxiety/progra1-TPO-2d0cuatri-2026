import datos

""" MOSTRAR DATOS """
# Anchos fijos, UNA sola vez, para usar los mismos en encabezado y en cada fila
ANCHO_CODIGO = 8
ANCHO_NOMBRE = 24
ANCHO_TEMA = 18
ANCHO_PUNTUACION = 12
ANCHO_DESCRIPCION = 35


def abreviar_texto(texto, ancho):
    # Si el texto no entra en el ancho, lo corta y le agrega "..." (usando slicing)
    if len(texto) > ancho:
        return texto[:ancho - 3] + "..."
    else:
        return texto


def mostrar_registros(matriz_peliculas):
    print("-" * 100)
    print(f"{'CODIGO':<{ANCHO_CODIGO}} {'NOMBRE':<{ANCHO_NOMBRE}} {'TEMA':<{ANCHO_TEMA}} {'PUNTUACION':<{ANCHO_PUNTUACION}} {'DESCRIPCION':<{ANCHO_DESCRIPCION}}")
    print("-" * 100)
    fila = len(matriz_peliculas)
    for i in range(fila):
        codigo = matriz_peliculas[i][0]
        nombre = matriz_peliculas[i][1]
        tema = matriz_peliculas[i][2]
        puntuacion = matriz_peliculas[i][3]
        descripcion = abreviar_texto(matriz_peliculas[i][4], ANCHO_DESCRIPCION)
        print(f"{codigo:<{ANCHO_CODIGO}} {nombre:<{ANCHO_NOMBRE}} {tema:<{ANCHO_TEMA}} {puntuacion:<{ANCHO_PUNTUACION}} {descripcion:<{ANCHO_DESCRIPCION}}")
    print("-" * 100)



""" CONSULTAR REGISTRO """ 
def busqueda_codigo (matriz_peliculas):
    codigo= int(input("Ingrese el codigo que quiere buscar: "))
    econtrado= False
    for i in range(len(matriz_peliculas)):
        if codigo == matriz_peliculas[i][0]:
            print("Codigo encontrado")
            print(matriz_peliculas[i])
            encontrado= True
            break
    if codigo == False:
        print("Codigo no encontrado")
    return codigo
    
    

