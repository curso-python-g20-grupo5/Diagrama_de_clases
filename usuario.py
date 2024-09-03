from listado_respuestas import ListadoRespuestas

class Usuario:
    """
    Representa un usuario que responde encuestas sobre mascotas.

    Atributos:
    ----------
    correo : str
        Correo electrónico del usuario.
    edad : int
        Edad del usuario.
    region : int
        Región geográfica del usuario.
    """

    def __init__(self, correo, edad, region):
        """
        Inicializa una nueva instancia de Usuario.

        Parámetros:
        -----------
        correo : str
            Correo electrónico del usuario.
        edad : int
            Edad del usuario.
        region : int
            Región geográfica del usuario.
        """
        self.correo = correo
        self.edad = edad
        self.region = region

    def contestar_encuesta(self, encuesta, respuestas):
        """
        Permite al usuario contestar una encuesta sobre mascotas agregando sus respuestas.

        Parámetros:
        -----------
        encuesta : Encuesta
            La encuesta a contestar.
        respuestas : list
            Lista de respuestas del usuario.
        """
        listado_respuestas = ListadoRespuestas(self, respuestas)
        encuesta.agregar_respuestas(listado_respuestas)
