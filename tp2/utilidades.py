def abreviar_texto(texto, ancho):
    # Si el texto no entra en el ancho, lo corta y le agrega "..." (usando slicing)
    if len(texto) > ancho:
        return texto[:ancho - 3] + "..."
    else:
        return texto

