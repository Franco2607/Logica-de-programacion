# Superclase
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def emitir_sonido(self):
        pass

# Subclases
class Perro(Animal):
    def emitir_sonido(self):
        return "¡Guau! ¡Guau!"

class Gato(Animal):
    def emitir_sonido(self):
        return "¡Miau! ¡Miau!"

# imprimir sonido
def imprimir_sonido_animal(animal):
    print(f"{animal.nombre} dice: {animal.emitir_sonido()}")

# Uso del código
mi_perro = Perro("Rex")
mi_gato = Gato("Luna")

imprimir_sonido_animal(mi_perro)
imprimir_sonido_animal(mi_gato)
 