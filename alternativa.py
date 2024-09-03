class Alternativa:
    """
    Representa una alternativa en una pregunta sobre mascotas.

    Atributos:
    ----------
    contenido : str
        Texto del contenido de la alternativa.
    ayuda : str, opcional
        Texto de ayuda adicional para la alternativa.
    """

    def __init__(self, contenido, ayuda=None):
        """
        Inicializa una nueva instancia de Alternativa.

        Parámetros:
        -----------
        contenido : str
            Texto del contenido de la alternativa.
        ayuda : str, opcional
            Texto de ayuda adicional para la alternativa.
        """
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar(self):
        """
        Muestra el contenido y la ayuda de la alternativa.

        Retorna:
        --------
        str
            Representación en texto del contenido y la ayuda.
        """
        return f"{self.contenido} (Ayuda: {self.ayuda})" if self.ayuda else self.contenido
