# funciones de menu
from crud import crear_registro, leer_registro, actualizar_registro, eliminar_registro, mostrar_todos_los_registros
from estadisticas import consultar_registros_por_categoria
from data import opciones_de_menu
from validaciones import validar_rango

def mostrar_menu():
  for opcion in opciones_de_menu:
    print(opcion)

def obtener_opcion():
  rango = (1, len(opciones_de_menu))
  opcion = input("Ingrese una opción: ")
  while not validar_rango(opcion, rango):
    print("Opción inválida. Intente de nuevo.")
    opcion = input("Ingrese una opción: ")
  return opcion

def ejecutar_opcion(opcion):
  if opcion == "1":
    crear_registro()
  elif opcion == "2":
    leer_registro()
  elif opcion == "3":
    actualizar_registro()
  elif opcion == "4":
    eliminar_registro()
  elif opcion == "5":
    mostrar_todos_los_registros()
  elif opcion == "6":
    consultar_registros_por_categoria()