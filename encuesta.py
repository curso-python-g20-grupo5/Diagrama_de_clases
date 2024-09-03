class Encuesta:
    """
    Representa una encuesta que contiene preguntas y respuestas sobre mascotas.

    Atributos:
    ----------
    nombre : str
        Nombre de la encuesta.
    preguntas : list
        Lista de preguntas contenidas en la encuesta.
    respuestas : list
        Lista de listas de respuestas de la encuesta.
    """

    def __init__(self, nombre, preguntas):
        """
        Inicializa una nueva instancia de Encuesta.

        Parámetros:
        -----------
        nombre : str
            Nombre de la encuesta.
        preguntas : list
            Lista de preguntas contenidas en la encuesta.
        """
        self.nombre = nombre
        self.preguntas = preguntas
        self.respuestas = []

    def mostrar(self):
        """
        Muestra la encuesta con sus preguntas y posibles respuestas.

        Retorna:
        --------
        str
            Representación en texto de la encuesta completa.
        """
        resultado = f"Encuesta: {self.nombre}\n"
        for pregunta in self.preguntas:
            resultado += f"{pregunta.mostrar()}\n"
        return resultado

    def agregar_respuestas(self, listado_respuestas):
        """
        Agrega un listado de respuestas a la encuesta.

        Parámetros:
        -----------
        listado_respuestas : ListadoRespuestas
            El listado de respuestas a agregar.
        """
        self.respuestas.append(listado_respuestas)


class EncuestaLimitadaEdad(Encuesta):
    """
    Representa una encuesta sobre mascotas limitada por rango de edad.

    Atributos:
    ----------
    edad_minima : int
        Edad mínima requerida para responder la encuesta.
    edad_maxima : int
        Edad máxima permitida para responder la encuesta.
    """

    def __init__(self, nombre, preguntas, edad_minima, edad_maxima):
        """
        Inicializa una nueva instancia de EncuestaLimitadaEdad.

        Parámetros:
        -----------
        nombre : str
            Nombre de la encuesta.
        preguntas : list
            Lista de preguntas contenidas en la encuesta.
        edad_minima : int
            Edad mínima requerida para responder la encuesta.
        edad_maxima : int
            Edad máxima permitida para responder la encuesta.
        """
        super().__init__(nombre, preguntas)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

    def agregar_respuestas(self, listado_respuestas):
        """
        Agrega un listado de respuestas a la encuesta, si cumple con las restricciones de edad.

        Parámetros:
        -----------
        listado_respuestas : ListadoRespuestas
            El listado de respuestas a agregar.
        """
        if self.edad_minima <= listado_respuestas.usuario.edad <= self.edad_maxima:
            super().agregar_respuestas(listado_respuestas)
        else:
            raise ValueError("El usuario no cumple con el rango de edad requerido.")


class EncuestaLimitadaRegion(Encuesta):
    """
    Representa una encuesta sobre mascotas limitada por región geográfica.

    Atributos:
    ----------
    regiones : list
        Lista de regiones permitidas para responder la encuesta.
    """

    def __init__(self, nombre, preguntas, regiones):
        """
        Inicializa una nueva instancia de EncuestaLimitadaRegion.

        Parámetros:
        -----------
        nombre : str
            Nombre de la encuesta.
        preguntas : list
            Lista de preguntas contenidas en la encuesta.
        regiones : list
            Lista de regiones permitidas para responder la encuesta.
        """
        super().__init__(nombre, preguntas)
        self.regiones = regiones

    def agregar_respuestas(self, listado_respuestas):
        """
        Agrega un listado de respuestas a la encuesta, si cumple con las restricciones de región.

        Parámetros:
        -----------
        listado_respuestas : ListadoRespuestas
            El listado de respuestas a agregar.
        """
        if listado_respuestas.usuario.region in self.regiones:
            super().agregar_respuestas(listado_respuestas)
        else:
            raise ValueError("El usuario no pertenece a una región permitida.")
