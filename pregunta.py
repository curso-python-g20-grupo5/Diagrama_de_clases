class Pregunta:
    """
    Representa una pregunta dentro de una encuesta sobre mascotas.

    Atributos:
    ----------
    enunciado : str
        Texto del enunciado de la pregunta.
    ayuda : str, opcional
        Texto de ayuda adicional para la pregunta.
    es_requerida : bool
        Indica si la pregunta es obligatoria o no.
    alternativas : list
        Lista de alternativas posibles para la pregunta.
    """

    def __init__(self, enunciado, es_requerida, alternativas, ayuda=None):
        """
        Inicializa una nueva instancia de Pregunta.

        Parámetros:
        -----------
        enunciado : str
            Texto del enunciado de la pregunta.
        es_requerida : bool
            Indica si la pregunta es obligatoria o no.
        alternativas : list
            Lista de alternativas posibles para la pregunta.
        ayuda : str, opcional
            Texto de ayuda adicional para la pregunta.
        """
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.es_requerida = es_requerida
        self.alternativas = alternativas

    def mostrar(self):
        """
        Muestra el enunciado, la ayuda y las alternativas de la pregunta.

        Retorna:
        --------
        str
            Representación en texto de la pregunta y sus alternativas.
        """
        resultado = f"{self.enunciado} (Ayuda: {self.ayuda})" if self.ayuda else self.enunciado
        for alternativa in self.alternativas:
            resultado += f"\n- {alternativa.mostrar()}"
        return resultado
