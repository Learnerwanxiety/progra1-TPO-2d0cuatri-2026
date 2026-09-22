def normalizar_texto_con_espacios(texto):
  return texto.strip()

def normalizar_texto_minusculas(texto):
  return texto.lower()

def normalizar_texto(texto):
  return normalizar_texto_minusculas(normalizar_texto_con_espacios(texto))

def capitalizar_texto(texto):
  return texto.capitalize()