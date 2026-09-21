import principal
import datos

opcion = -1

while opcion != 0:
    print("---" * 20)
    print("1- Mostrar todos los registros")
    print("2- Consultar un registro por código")
    print("3- Generar una vista previa del texto")
    print("4- Normalizar y transformar un texto")
    print("5- Consultar registros por palabra o expresión")
    print("6- Separar y reconstruir un texto")
    print("7- Consultar registros por categoría")
    print("8- Procesamiento estadístico")
    print("0- Salir")
    print("---" * 20)

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        principal.mostrar_registros(datos.matriz_peliculas)

    elif opcion == 2:
        principal.busqueda_codigo (datos.matriz_peliculas)

    elif opcion == 3:
        print("Generar una vista previa del texto")

    elif opcion == 4:
        print("Normalizar y transformar un texto")

    elif opcion == 5:
        print("Consultar registros por palabra o expresión")

    elif opcion == 6:
        print("Separar y reconstruir un texto")

    elif opcion == 7:
        print("Consultar registros por categoría")

    elif opcion == 8:
        print("Procesamiento estadístico")

    elif opcion == 0:
        print("Programa finalizado.")

    else:
        print("Opción inválida.")
        
    

