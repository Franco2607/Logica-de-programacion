# Establece que si tenemos una clase y esta clase tiene otra clase o clases derivadad
# Los objetos de la clase base (La super clase) nos podemos alternar sin que el 
# Funcionamiento de nuestro programa sea incorrecto

# Super() es una función que permite acceder a métodos y atributos de la clase pader
# desde una hija

# Incorrecto


class ave:
    def fly(self):
        return "Vuela"


class Gallina(ave):
    def fly(self):
        raise Exception("Los pollos no vuelan")


# ave = ave()
# ave.fly()
# Gallina = Gallina()
# Gallina.fly()

# Correcto

class ave:
    def move(self):
        return "Se mueve"


class Gallina(ave):
    def move(self):
        return "Camina"


ave = ave()
print(ave.move())
Gallina = Gallina()
print(Gallina.move())

# ave = Gallina()
# print(ave.move())
# Gallina = ave()
# print(Gallina.move())

# Extra

class Vehiculo:

    def __init__(self, velocidad=0):
        self.velocidad = velocidad

    def aceleracion(self, incrementa):
        self.velocidad += incrementa
        print(f"Velocidad: {self.velocidad} Km/h")

    def frenar(self, decrementa):
        self.velocidad -= decrementa
        if self.velocidad <= 0:
            self.velocidad = 0
        print(f"Velocidad: {self.velocidad} Km/h")


class Carro(Vehiculo):
    def aceleracion(self, incrementa):
        print("El coche está acelerando")
        super().aceleracion(incrementa)

    def frenar(self, decrementa):
        print("El coche está frenando")
        super().frenar(decrementa)


class Bicicleta(Vehiculo):
    def aceleracion(self, incrementa):
        print("La bicicleta está acelerando")
        super().aceleracion(incrementa)

    def frenar(self, decrementa):
        print("La bicicleta está frenando")
        super().frenar(decrementa)


class Moto(Vehiculo):
    def aceleracion(self, incrementa):
        print("La moto está acelerando")
        super().aceleracion(incrementa)

    def frenar(self, decrementa):
        print("La moto está frenando")
        super().frenar(decrementa)


def test_Vehiculo(Vehiculo):
    Vehiculo.aceleracion(2)
    Vehiculo.frenar(1)


Carro = Carro()
Bicicleta = Bicicleta()
Moto = Moto()

test_Vehiculo(Carro)
test_Vehiculo(Bicicleta)
test_Vehiculo(Moto)