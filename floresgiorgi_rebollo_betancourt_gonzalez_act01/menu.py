import crud
import estadisticas
import validaciones

def mostrar_menu():
    print("\n===== GESTIÓN DE GIMNASIO =====")
    print("1. Dar de alta un socio")
    print("2. Consultar un socio")
    print("3. Modificar un socio")
    print("4. Eliminar un socio")
    print("5. Mostrar todos los socios")
    print("6. Consultar socios por actividad")
    print("7. Ver estadísticas")
    print("8. Salir")

def ejecutar_menu(matriz, actividades, estados):

    opcion = ""
    while opcion != "8":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        while not validaciones.opcion_valida(opcion, 1, 8):
            print("Opción inválida.")
            opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crud.alta_socio(matriz, actividades, estados)
        elif opcion == "2":
            crud.consultar_socio(matriz)
        elif opcion == "3":
            crud.modificar_socio(matriz, actividades, estados)
        elif opcion == "4":
            crud.eliminar_socio(matriz)
        elif opcion == "5":
            crud.mostrar_socios(matriz, 12)
        elif opcion == "6":
            crud.consultar_por_actividad(matriz, actividades)
        elif opcion == "7":
            estadisticas.mostrar_estadisticas(matriz, actividades)
        elif opcion == "8":
            print("Saliendo del sistema...")
