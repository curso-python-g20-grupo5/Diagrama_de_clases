class ListadoRespuestas:
    """
    Representa un conjunto de respuestas dado por un usuario para una encuesta sobre mascotas.

    Atributos:
    ----------
    usuario : Usuario
        El usuario que generó las respuestas.
    respuestas : list
        Lista de respuestas del usuario.
    """

    def __init__(self, usuario, respuestas):
        """
        Inicializa una nueva instancia de ListadoRespuestas.

        Parámetros:
        -----------
        usuario : Usuario
            El usuario que generó las respuestas.
        respuestas : list
            Lista de respuestas del usuario.
        """
        self.usuario = usuario
        self.respuestas = respuestas
