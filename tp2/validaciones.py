- El nombre debe contener solamente letras y tener al menos 3 caracteres.
- El legajo debe contener solamente números.
- El nombre de usuario debe contener solamente letras y números y tener al menos 6 caracteres.
'''

def validar_nombre(nombre):
    valido = False
    if nombre.isalpha() and len(nombre) >= 3:
        valido = True
    return valido

def validar_legajo(legajo):
    return legajo.isdigit()

def validar_usuario(usuario):
    valido = False
    if usuario.isalnum() and len(usuario) >= 6:
        valido = True
    return valido

# Programa principal
nombre = input("Ingrese nombre (3 o más letras): ")
while not validar_nombre(nombre):
    print("Nombre inválido, debe tener 3 o más letras.")
    nombre = input("Ingrese nombre (3 o más letras): ")

legajo = input("Ingrese legajo (solo números): ")
while not validar_legajo(legajo):
    print("Legajo inválido, debe tener solamente números.")
    legajo = input("Ingrese legajo (solo números): ")

usuario = input("Ingrese nombre de usuario (6 o más caracteres, solamente letras y números): ")
while not validar_usuario(usuario):
    print("Nombre de usuario inválido, debe contener 6 o más caracteres y solamente letras y números.")    
    usuario = input("Ingrese nombre de usuario (6 o más caracteres, solamente letras y números): ")

print("-"*30)
print("Nombre:", nombre)
print("Legajo:", legajo)
print("Usuario:", usuario)
print("-"*30)
