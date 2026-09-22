"""
Módulo encargado de proporcionar los datos iniciales del sistema.
Temática: Reseñas de películas y series.
"""


def obtener_registros():
    """
    Retorna la matriz con los 10 registros iniciales de reseñas de
    películas y series.

    Cada registro tiene el formato:
    [Código, Título, Género, Puntuación, Reseña]
    """
    registros = [
        [101, "El viaje interminable", "Drama", "4",
         "Una historia profunda con actuaciones memorables y un final que emociona"],
        [102, "Risas en la oficina", "Comedia", "3",
         "Una comedia liviana con buenos diálogos aunque el ritmo decae hacia el final"],
        [103, "Sombras del pasado", "Terror", "5",
         "Una historia de suspenso con actuaciones sólidas que mantiene la tensión de principio a fin"],
        [104, "Mundos paralelos", "Ciencia ficción", "4",
         "Una premisa original con efectos visuales notables y una historia bien desarrollada"],
        [105, "Amor en Buenos Aires", "Romance", "3",
         "Una historia sencilla con buenas actuaciones pero un desarrollo previsible"],
        [106, "La última frontera", "Aventura", "5",
         "Una aventura con paisajes impresionantes y una historia que atrapa desde el inicio"],
        [107, "Noches sin dormir", "Terror", "2",
         "Una historia con buenas ideas pero actuaciones flojas que restan tensión"],
        [108, "Segunda oportunidad", "Drama", "5",
         "Una historia conmovedora con actuaciones memorables y un guion muy bien escrito"],
        [109, "El detective silencioso", "Misterio", "4",
         "Una trama de suspenso con giros interesantes y una historia bien construida"],
        [110, "Risas compartidas", "Comedia", "4",
         "Una comedia con buenos diálogos y actuaciones que generan muchas risas"]
    ]
    return registros
