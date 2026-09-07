"""
este modulos se encarga de: 
funciones relacionadas al menú y sus posibles opciones
"""
def  menu_modificacion():
    print( """
    1.Ingrese 1 para modificar 'nombre'
    2.Ingrese 2 para modificar 'actividad'
    3.Ingrese 3 para modificar 'Valor de Cuota'
    4.Ingrese 4 para modificar 'estado'
""")
    opcion = int(input("Ingrese la opción elegida: "))
    return(opcion)