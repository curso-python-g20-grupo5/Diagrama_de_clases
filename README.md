# Sistema de Encuestas sobre Mascotas

Este proyecto es una implementación de un sistema de encuestas centrado en la temática de mascotas. Fue desarrollado como parte de un desafío para aplicar conceptos de diagramas de clases y programación orientada a objetos en Python.

## Descripción del Proyecto

El objetivo de este proyecto es crear un sistema que permita a los usuarios responder encuestas sobre mascotas. El sistema está diseñado considerando las relaciones entre usuarios, encuestas, preguntas, alternativas y respuestas. 

### Funcionalidades Principales

- **Usuarios**: Los usuarios pueden contestar encuestas y sus respuestas son almacenadas y asociadas a su perfil.
- **Encuestas**: Se pueden crear encuestas con preguntas sobre mascotas, incluyendo encuestas limitadas por edad y región.
- **Preguntas y Alternativas**: Cada encuesta puede contener múltiples preguntas, cada una con un conjunto de alternativas para que el usuario seleccione su respuesta.
- **Respuestas**: Las respuestas de los usuarios se almacenan y son accesibles para su posterior análisis.

## Estructura del Código

- `alternativa.py`: Define la clase `Alternativa`, que representa una posible respuesta en una pregunta.
- `pregunta.py`: Contiene la clase `Pregunta`, que encapsula el enunciado de una pregunta y sus posibles alternativas.
- `encuesta.py`: Implementa la clase `Encuesta` y sus subclases `EncuestaLimitadaEdad` y `EncuestaLimitadaRegion`, que representan las encuestas y sus variaciones con restricciones.
- `usuario.py`: Define la clase `Usuario`, que representa a un usuario que puede responder encuestas.
- `listado_respuestas.py`: Contiene la clase `ListadoRespuestas`, que almacena las respuestas de un usuario a una encuesta.
- `main.py`: Script principal que muestra cómo se utilizan las clases para crear y responder una encuesta.

## Diagrama de Clases

El diagrama de clases completo del sistema está disponible en el archivo `diagrama_clases_final.md`.

## Ejecución

Para ejecutar el proyecto, simplemente corre el archivo `main.py`:

```bash
python main.py
```


## Autores y Autoras

- [Esteban Hernández](https://github.com/stivhc)
- [Valery Maragaño](https://github.com/Valyxp)
- [Rosa Rubio](https://github.com/PaulinaRubioP)
- [Marco Alvarado](https://github.com/7pixel-cl)


⌨️ con ❤️ por el Grupo 5 - G20 😊
