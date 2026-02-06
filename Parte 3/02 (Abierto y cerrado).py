# Abierto para la extension (Significa que se pueden añadir nuevas funcionalidades 
# sin modificar el codigo existente)
# cerrado para la modificación (A medida que vamos avanzando no debemos modificarlo)


from abc import ABC, abstractmethod

# Se importa ABC para crear clases abstractas
# Se importa abstractmethod para crear metodos y funciones abstractas


class Form:
    def dibujar(self):
        pass


class cuadrado(Form):
    def dibujar(self):
        print("Dibuja un cuadrado")


class circulo(Form):
    def dibujar(self):
        print("Dibuja un círculo")


class triangulo(Form):
    def dibujar(self):
        print("Dibuja un triángulo")

# Extra

class Operacion(ABC):
    @abstractmethod
    def ejecutar(self, a, b):
        pass


class Adicion(Operacion):
    def ejecutar(self, a, b):
        return a + b


class Sustraccion(Operacion):
    def ejecutar(self, a, b):
        return a - b


class Multiplication(Operacion):
    def ejecutar(self, a, b):
        return a * b


class Division(Operacion):
    def ejecutar(self, a, b):
        return a / b


class Potencia(Operacion):
    def ejecutar(self, a, b):
        return a ** b


class Calculator:
    def __init__(self) -> None:
        self.operacion = {}

    def add_operacion(self, name, Operacion):
        self.operacion[name] = Operacion

    def Calcular(self, name, a, b): 
        if name not in self.operacion:
            raise ValueError(f"La operación {name} no está soportada.")
        return self.operacion[name].ejecutar(a, b)

# Añadirle la capacidad para que haga las operaciones sin modificar la calculadora
calculator = Calculator()
calculator.add_operacion("Adicion", Adicion())
calculator.add_operacion("Sustraccion", Sustraccion())
calculator.add_operacion("multiplication", Multiplication())
calculator.add_operacion("division", Division())
calculator.add_operacion("Potencia", Potencia())

print(calculator.Calcular("Adicion", 10, 5))
print(calculator.Calcular("Sustraccion", 10, 5))
print(calculator.Calcular("multiplication", 10, 5))
print(calculator.Calcular("division", 10, 5))
print(calculator.Calcular("Potencia", 10, 5))