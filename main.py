from alternativa import Alternativa
from pregunta import Pregunta
from encuesta import Encuesta
from usuario import Usuario
from listado_respuestas import ListadoRespuestas

def obtener_respuesta_usuario(pregunta):
    """
    Muestra una pregunta al usuario y obtiene su respuesta.

    Parámetros:
    -----------
    pregunta : Pregunta
        La pregunta que se hará al usuario.

    Retorna:
    --------
    int
        Índice de la respuesta seleccionada por el usuario.
    """
    print(pregunta.enunciado)
    if pregunta.ayuda:
        print(f"Ayuda: {pregunta.ayuda}")

    for i, alternativa in enumerate(pregunta.alternativas):
        print(f"{i + 1}. {alternativa.mostrar()}")

    while True:
        try:
            respuesta = int(input("Seleccione una opción (número): ")) - 1
            if 0 <= respuesta < len(pregunta.alternativas):
                return respuesta
            else:
                print("Por favor, seleccione un número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def main():
    # Crear alternativas sobre mascotas
    alt1 = Alternativa("Perro", "Un animal muy leal")
    alt2 = Alternativa("Gato", "Un animal muy independiente")
    alt3 = Alternativa("Pez", "Una mascota tranquila")

    # Crear preguntas sobre mascotas
    pregunta1 = Pregunta("¿Cuál es tu mascota favorita?", True, [alt1, alt2, alt3], "Elige una opción")
    pregunta2 = Pregunta("¿Cuántas mascotas tienes?", True, [Alternativa("1"), Alternativa("2"), Alternativa("3 o más")])

    # Crear encuesta sobre mascotas
    encuesta = Encuesta("Encuesta sobre mascotas", [pregunta1, pregunta2])

    # Crear usuario
    usuario = Usuario("user@example.com", 30, 1)

    # Recoger respuestas del usuario en tiempo real
    respuestas = []
    for pregunta in encuesta.preguntas:
        respuesta = obtener_respuesta_usuario(pregunta)
        respuestas.append(respuesta)

    # Usuario responde la encuesta con las respuestas recogidas
    usuario.contestar_encuesta(encuesta, respuestas)

    # Mostrar la encuesta con las respuestas
    print("\nRespuestas registradas:")
    print(encuesta.mostrar())

    # Mensaje final
    print("¡Gracias por completar la encuesta!")

if __name__ == "__main__":
    main()