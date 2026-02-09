import random

casas = {
    "Frontend": 0,
    "Backend": 0,
    "Mobile": 0,
    "Data": 0
}

preguntas = [
    {
        "pregunta": "¿Qué área te gustaría fortalecer más?",
        "respuestas": [
            {
                "opcion": "Programación del servidor.",
                "casa": "Backend"
            },
            {
                "opcion": "Desarrollo móvil.",
                "casa": "Mobile"
            },
            {
                "opcion": "Diseño web.",
                "casa": "Frontend"
            },
            {
                "opcion": "Análisis de información.",
                "casa": "Data"
            }
        ]
    },
    {
        "pregunta": "Cuando algo no funciona, ¿qué haces primero?",
        "respuestas": [
            {
                "opcion": "Probar la app en distintos celulares.",
                "casa": "Mobile"
            },
            {
                "opcion": "Revisar el diseño y comportamiento visual.",
                "casa": "Frontend"
            },
            {
                "opcion": "Verificar la información procesada.",
                "casa": "Data"
            },
            {
                "opcion": "Analizar la lógica del programa.",
                "casa": "Backend"
            }
        ]
    },
    {
        "pregunta": "¿Qué te motiva más al terminar una tarea?",
        "respuestas": [
            {
                "opcion": "Obtener resultados claros a partir de datos.",
                "casa": "Data"
            },
            {
                "opcion": "Probar una app móvil que funciona sin fallos.",
                "casa": "Mobile"
            },
            {
                "opcion": "Saber que el sistema es estable.",
                "casa": "Backend"
            },
            {
                "opcion": "Ver una interfaz bonita y funcional.",
                "casa": "Frontend"
            }
        ]
    },
    {
        "pregunta": "¿Qué tipo de problemas prefieres resolver?",
        "respuestas": [
            {
                "opcion": "Errores de sistema y rendimiento.",
                "casa": "Backend"
            },
            {
                "opcion": "Fallos en aplicaciones móviles.",
                "casa": "Mobile"
            },
            {
                "opcion": "Detalles visuales y experiencia del usuario.",
                "casa": "Frontend"
            },
            {
                "opcion": "Datos incompletos o inconsistentes.",
                "casa": "Data"
            }
        ]
    },
    {
        "pregunta": "¿Cuál de estas actividades te resulta más interesante?",
        "respuestas": [
            {
                "opcion": "Programar funcionalidades móviles.",
                "casa": "Mobile"
            },
            {
                "opcion": "Interpretar información numérica.",
                "casa": "Data"
            },
            {
                "opcion": "Gestionar bases de datos y servidores.",
                "casa": "Backend"
            },
            {
                "opcion": "Diseñar interfaces agradables.",
                "casa": "Frontend"
            }
        ]
    },
    {
        "pregunta": "¿Cómo mides que hiciste un buen trabajo?",
        "respuestas": [
            {
                "opcion": "Cuando la app corre fluida.",
                "casa": "Mobile"
            },
            {
                "opcion": "Cuando los datos son claros y útiles.",
                "casa": "Data"
            },
            {
                "opcion": "Cuando el sistema responde rápido.",
                "casa": "Backend"
            },
            {
                "opcion": "Cuando el diseño se ve profesional.",
                "casa": "Frontend"
            }
        ]
    },
    {
        "pregunta": "¿Qué prefieres aprender primero?",
        "respuestas": [
            {
                "opcion": "Análisis y visualización de datos.",
                "casa": "Data"
            },
            {
                "opcion": "Herramientas para apps móviles.",
                "casa": "Mobile"
            },
            {
                "opcion": "Frameworks de interfaces.",
                "casa": "Frontend"
            },
            {
                "opcion": "Arquitectura de servidores.",
                "casa": "Backend"
            }
        ]
    },
    {
        "pregunta": "¿Qué parte de un proyecto disfrutas más?",
        "respuestas": [
            {
                "opcion": "Resolver la lógica interna del sistema.",
                "casa": "Backend"
            },
            {
                "opcion": "Hacer que una app funcione bien en diferentes dispositivos.",
                "casa": "Mobile"
            },
            {
                "opcion": "Analizar datos y encontrar patrones.",
                "casa": "Data"
            },
            {
                "opcion": "Diseñar la experiencia del usuario.",
                "casa": "Frontend"
            }
        ]
    },
    {
        "pregunta": "En un equipo de desarrollo, ¿qué rol te imaginas teniendo?",
        "respuestas": [
            {
                "opcion": "Analista de datos.",
                "casa": "Data"
            },
            {
                "opcion": "Desarrollador de aplicaciones móviles.",
                "casa": "Mobile"
            },
            {
                "opcion": "Responsable del funcionamiento del sistema.",
                "casa": "Backend"
            },
            {
                "opcion": "Encargado del diseño visual.",
                "casa": "Frontend"
            }
        ]
    },
    {
        "pregunta": "¿Qué tipo de tareas te llaman más la atención al programar?",
        "respuestas": [
            {
                "opcion": "Trabajar con información y sacar conclusiones útiles.",
                "casa": "Data"
            },
            {
                "opcion": "Desarrollar aplicaciones para teléfonos.",
                "casa": "Mobile"
            },
            {
                "opcion": "Construir servicios y manejar la lógica del sistema.",
                "casa": "Backend"
            },
            {
                "opcion": "Crear pantallas interactivas y bien diseñadas.",
                "casa": "Frontend"
            }
        ]
    }
]



print("\n¡Bienvenido a Hogwarts, la escuela de programación para magos y brujas del código!")
print("El sombrero seleccionador decidirá cuál es tu casa como programador.")

name = input("\n¿Cuál es tu nombre? ")

# Este bucle for recorre todas las preguntas del cuestionario "preguntas".
# Para cada pregunta:
#   1. Muestra por pantalla la pregunta correspondiente (con su número).
#   2. Muestra todas las posibles respuestas para esa pregunta, numeradas del 1 al 4.
#   3. Solicita al usuario que seleccione una opción introduciendo un número del 1 al 4.
#   4. Según la opción elegida por el usuario, incrementa el contador de la casa correspondiente en el diccionario "casas".
for index, pregunta in enumerate(preguntas):
    print(f"\nPregunta {index + 1}: {pregunta['pregunta']}\n")

    for i, answer in enumerate(pregunta["respuestas"]):
        print(f"{i + 1}. {answer['opcion']}")

    eleccion = int(input("\nSelecciona una respuesta entre 1 y 4: "))

    seleccion_respuesta = pregunta["respuestas"][eleccion - 1]
    casas[seleccion_respuesta["casa"]] += 1

asignar_casa = max(casas, key=casas.get)
puntaje = list(casas.values())

if puntaje.count(max(puntaje)) > 1:
    posibles_casas = [
        casa for casa,
        points in casas.items() if points == max(puntaje)
    ]
    asignar_casa = random.choice(posibles_casas)

    print(
        f"""\nHmmmm... Ha sido una decisión muy complicada, {
            name}.\n¡Pero finalmente tu casa será {asignar_casa}!"""
    )
else:
    print(f"\nEnhorabuena, {name}.\n¡Tu casa será {asignar_casa}!")