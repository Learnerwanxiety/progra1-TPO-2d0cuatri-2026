# aplicacion.py
# Programa principal: inicializa los datos y coordina el funcionamiento
# del sistema de gestión de gimnasio.

import datos
import menu


def main():
    matriz = datos.cargar_datos_iniciales()
    actividades = datos.obtener_actividades()
    estados = datos.obtener_estados()

    menu.ejecutar_menu(matriz, actividades, estados)


main()
