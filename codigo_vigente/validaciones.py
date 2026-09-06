# funciones de validacion

def validar_registro(registro):
  raise NotImplementedError("No Implementado")

def validar_input(input):
  raise NotImplementedError("No Implementado")

def validar_rango(valor, rango):
  try:
    numero = int(valor)
  except (TypeError, ValueError):
    return False
  minimo, maximo = rango
  return minimo <= numero <= maximo