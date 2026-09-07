from data import socios
from menu import menu_modificacion

def alta(registros):
    nombre = input("Ingrese el nombre del socio: ")
    Actividad_Principal= input("Ingrese la actividad principal del socio: ")
    Valor_Cuota= float(input("Ingrese el valor de la cuota del cliente: "))
    if registros:
        nuevo_id = registros[-1][0] + 1  
    else:
        nuevo_id = 1  
    nuevo_usuario = [nuevo_id, nombre,  Actividad_Principal, Valor_Cuota]
    registros.append(nuevo_usuario)

    return registros



def consulta (registros):
    nombre_usuario = input("Ingrese el nombre del usuario: ")
    for i in range(len(registros)):
        if registros[i][1] == nombre_usuario:
            return(registros[i])
    return(False)

def modificar_socio(socios):
    id_buscar = int(input("Ingrese el ID del socio a modificar: "))
    
    # Recorremos la matriz buscando el ID
    for i in range(len(socios)):
        if socios[i][0] == id_buscar:
            print("\nSocio encontrado: " + str(socios[i]))
            print("Ingrese los nuevos datos (deje en blanco y presione ENTER para no modificar):")
            
            # Pedimos los nuevos datos
            nuevo_nombre = input("Nuevo nombre [" + str(socios[i][1]) + "]: ")
            nueva_actividad = input("Nueva actividad [" + str(socios[i][2]) + "]: ")
            nuevo_estado = input("Nuevo estado (Activo/Inactivo) [" + str(socios[i][4]) + "]: ")
            
            # Si el usuario ingresó un valor, actualizamos la columna correspondiente
            if nuevo_nombre != "":
                socios[i][1] = nuevo_nombre
                
            if nueva_actividad != "":
                socios[i][2] = nueva_actividad
                    
            if nuevo_estado != "":
                socios[i][4] = nuevo_estado
                
            print("\n¡Socio modificado con éxito!")
            print("Registro actualizado: " + str(socios[i]))
            return True
            
    print("\nNo se encontró ningún socio con el ID ingresado.")
    return False

def modificar_cuota(registros):
    porcentaje = float(input("Ingrese cuál es el porcentaje de aumento: ")) / 100
    for i in range(len(registros)):
        registros[i][3] += registros[i][3] * porcentaje
    

def eliminacion(registros):
    usuario = consulta(registros)
    if usuario != False: 
        registros.remove(usuario)
        print("Usuario borrado con éxito")
    else:
        print("El usuario que busca no existe")
