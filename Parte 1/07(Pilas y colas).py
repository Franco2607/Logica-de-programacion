# Pilas
# LIFO significa Last In, First Out (El último en entrar es el primero en salir)

pila = []
pila.append("Plato 1")
pila.append("Plato 2")
ultimo = pila.pop()

print(pila)

# Colas
# FIFO significa First In, First Out (El primero en entrar es el primero en salir)

cola = []
cola.append("Persona 1")
cola.append("Persona 2")
primero = cola.pop(0)

print(cola)

# EXTRA

# Pila

# Web


def web_navigation():

    stack = []

    while True:

        action = input(
            "Añade una url o interactúa con palabras adelante/atrás/salir: "
        )

        if action == "salir":
            print("Saliendo del navegador web.")
            break
        elif action == "adelante":
            pass
        elif action == "atrás":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"Has navegado a la web: {stack[len(stack) - 1]}.")
        else:
            print("Estás en la página de inicio.")


web_navigation()


def shared_printed():

    cola = []

    while True:

        action = input("Añade un colaumento o selecciona imprimir/salir: ")

        if action == "salir":
            break
        elif action == "imprimir":
            if len(cola) > 0:
                print(f"Imprimiendo: {cola.pop(0)}")
        else:
            cola.append(action)

        print(f"Cola de impresión: {cola}")


shared_printed()  