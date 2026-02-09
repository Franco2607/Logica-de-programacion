import random


class Participante:

    def __init__(self, name, pais):
        self.name = name
        self.pais = pais

# eq es un equal podemos desarrollar una logica que le indique a una clase que es para esta 
# clase un objeto igual

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Participante):
            return self.name == other.name and self.pais == other.pais
        return False

# algoritmo funcional que convierte cualquier cantidad de datos (texto, archivos) en una 
# secuencia alfanumérica única y de tamaño fijo, conocida como "huella digital" o resumen

    def __hash__(self) -> int:
        return hash((self.name, self.pais))

class Olympics:

    def __init__(self):
        self.eventos = []
        self.participantes = {}
        self.evento_resultados = {}
        self.pais_resultados = {}

    def registrar_evento(self):

        evento = input("Introduce el nombre del evento deportivo: ").strip()

        if evento in self.eventos:
            print(f"El evento {evento} ya está registrado.")
        else:
            self.eventos.append(evento)
            print(f"Evento {evento} registrado correctamente.")

    def registrar_participante(self):
        if not self.eventos:
            print("No hay eventos registrados. Por favor, registra uno primero.")
            return

        name = input("Introduce el nombre del participante: ").strip()
        pais = input("Introduce el país del participante: ").strip()
        participante = Participante(name, pais)

        print("Eventos deportivos disponibles:")
        # 'enumerate' es una función que te da tanto el índice (posición) como el elemento 
        # (evento) al recorrer una lista.
        # 'index' representa la posición actual (empezando en 0) y 'evento' es el valor 
        # correspondiente en cada iteración.
        for index, evento in enumerate(self.eventos):
            print(f"{index + 1}. {evento}")

        elegir_evento = int(
            input("Selecciona el número del evento para asignar al participante: ")) - 1

        if elegir_evento >= 0 and elegir_evento < len(self.eventos):

            evento = self.eventos[elegir_evento]

            if evento in self.participantes and participante in self.participantes[evento]:
                print(
                    f"El participante {name} de {pais} ya está registrado en el evento deportivo {evento}.")
            else:

                if evento not in self.participantes:
                    self.participantes[evento] = []

                self.participantes[evento].append(participante)
                print(
                    f"El participante {name} de {pais} se ha registrado en el evento deportivo {evento}.")
        else:
            print(
                "Selección de evento deportivo inválido. El participante no se ha registrado.")

    def simular_eventos(self):

        if not self.eventos:
            print("No hay eventos registrados. Por favor, registra uno primero.")
            return

        for evento in self.eventos:

            if len(self.participantes[evento]) < 3:
                print(
                    f"No hay participantes suficientes para simular el evento {evento} (mínimo 3).")
                continue

# Sample indica que solo se va a quedar con 3 de todos los participantes
# shuffle baraja los participantes de una manera aleatoria para oro, plata y bronce

            evento_participantes = random.sample(self.participantes[evento], 3)
            random.shuffle(evento_participantes)

            gold, silver, bronze = evento_participantes
            self.evento_resultados[evento] = [gold, silver, bronze]

            self.resultado_pais(gold.pais, "gold")
            self.resultado_pais(silver.pais, "silver")
            self.resultado_pais(bronze.pais, "bronze")

            print(f"Resultados simulación del evento: {evento}")
            print(f"Oro: {gold.name} ({gold.pais})")
            print(f"Plata: {silver.name} ({silver.pais})")
            print(f"Bronce: {bronze.name} ({bronze.pais})")

    def resultado_pais(self, pais, medalla):
        if pais not in self.pais_resultados:
            self.pais_resultados[pais] = {
                "gold": 0, "silver": 0, "bronze": 0}
        self.pais_resultados[pais][medalla] += 1

    def mostrar_reporte(self):

        print("Informe Juegos Olímpicos:")

        if self.evento_resultados:

            print("Informe por evento:")
 
            for evento, winners in self.evento_resultados.items():
                print(f"Evento: {evento}")
                print(f"Oro: {winners[0].name} ({winners[0].pais})")
                print(f"Plata: {winners[1].name} ({winners[1].pais})")
                print(f"Bronce: {winners[2].name} ({winners[2].pais})")
        else:
            print("No hay resultados registrados.")

        print()

        if self.pais_resultados:

            print("Informe por país:")

            for pais, medals in sorted(self.pais_resultados.items(), key=lambda x: (
                    x[1]["gold"], x[1]["silver"], x[1]["bronze"]), reverse=True):

                print(
                    f"{pais}: Oro {medals['gold']}, Plata {medals['silver']}, Bronce {medals['bronze']}")

        else:
            print("No hay medallas por país registradas.")


olympics = Olympics()

print("Simulador de Juegos Olímpicos")

while True:

    print()

    print("1. Registro de eventos")
    print("2. Registro de participantes")
    print("3. Simulación de eventos")
    print("4. Creación de informes")
    print("5. Salir")

    option = input("Selecciona una acción: ")

    match option:
        case "1":
            olympics.registrar_evento()
        case "2":
            olympics.registrar_participante()
        case "3":
            olympics.simular_eventos()
        case "4":
            olympics.mostrar_reporte()
        case "5":
            print("Saliendo del simulador...")
            break
        case _:
            print("Opción inválida. Por favor, selecciona una nueva.")