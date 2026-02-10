import random


class luchador:
    def __init__(self, name: str, velocidad: int, ataque: int, defensa: int):
        self.name = name
        self.velocidad = velocidad
        self.ataque = ataque
        self.defensa = defensa
        self.vida = 100

    def reiniciar_vida(self):
        self.vida = 100

    def con_vida(self) -> bool:
        return self.vida > 0

    def recibir_daño(self, daño: int):

        daño_de_ataque = 0

        if random.random() < 0.2:
            print(f"{self.name} ha esquivado el ataque")
        else:
            if self.defensa >= daño:
                daño_de_ataque = daño * 0.1
            else:
                daño_de_ataque = daño - self.defensa

            daño_de_ataque = int(daño_de_ataque)

        self.vida = max(self.vida - daño_de_ataque, 0)
        print(f"{self.name} ha recibido {daño_de_ataque} de daño")
        print(f"Salud restante de {self.name}: {self.vida}")


class Batalla:

    def __init__(self, luchador1: luchador, luchador2: luchador):
        self.luchador1 = luchador1
        self.luchador2 = luchador2

    def pelea(self) -> luchador:

        print(f"\n=== {self.luchador1.name} vs. {self.luchador2.name} ===")

        while self.luchador1.con_vida() and self.luchador2.con_vida():

            if self.luchador1.velocidad >= self.luchador2.velocidad:
                self.turno(self.luchador1, self.luchador2)
                if self.luchador2.con_vida():
                    self.turno(self.luchador2, self.luchador1)
            else:
                self.turno(self.luchador2, self.luchador1)
                if self.luchador1.con_vida():
                    self.turno(self.luchador1, self.luchador2)

        if self.luchador1.con_vida():
            print(f"\n{self.luchador1.name} es el ganador de la batalla")
            return self.luchador1
        else:
            print(f"\n{self.luchador2.name} es el ganador de la batalla")
            return self.luchador2

    def turno(self, ataqueer: luchador, defender: luchador):
        print(f"\n{ataqueer.name} ataca a {defender.name}")
        defender.recibir_daño(ataqueer.ataque)


class Torneo:

    def __init__(self, luchadores: list):
        if not self.potencia_de_dos(len(luchadores)):
            raise ValueError(
                "El número de luchadores debe ser una potencia de 2")
        self.luchadores = luchadores

    def inicio(self):
        round = 1
        while len(self.luchadores) > 1:

            print(f"\n=== Ronda {round} ===")

            random.shuffle(self.luchadores)

            ganadores = []

            for index in range(0, len(self.luchadores), 2):
                luchador1 = self.luchadores[index]
                luchador2 = self.luchadores[index + 1]

                Batallas = Batalla(luchador1, luchador2)
                winner = Batallas.pelea()
                winner.reiniciar_vida()
                ganadores.append(winner)

            self.luchadores = ganadores
            round += 1

        print(f"\n¡El ganador del torneo es {self.luchadores[0].name}!")

    def potencia_de_dos(self, n) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1


luchadores = [
    luchador("Goku", 90, 98, 90),
    luchador("Vegeta", 95, 90, 82),
    luchador("Piccolo", 80, 85, 90),
    luchador("Freezer", 95, 90, 75), 
    luchador("Krillin", 95, 90, 75),
    luchador("Cell", 92, 70, 73),
    luchador("Gohan", 97, 95, 70),
    luchador("Trunks", 88, 88, 88)
]

Torneo = Torneo(luchadores)
Torneo.inicio()