import random


class ArbolNavidad:

    def __init__(self, altura: int):

        self.altura = altura
        self.arbol = [
            [" " for _ in range(2 * altura - 1)]
            for _ in range(altura)
        ]

        for i in range(altura):
            for j in range(altura - i - 1, altura + i):
                self.arbol[i][j] = "*"

        self.trunk = [
            [" " for _ in range(2 * altura - 1)]
            for _ in range(2)
        ]

        for i in range(2):
            for j in range(altura - 2, altura + 1):
                self.trunk[i][j] = "|"

        self.estrella = False
        self.bolas = []
        self.luces = []
        self.luces_on = False

    def display_arbol(self):
        for index, row in enumerate(self.arbol):
            if index == 0 and self.estrella:
                print("".join(row).replace("*", "@"))
            else:
                print("".join(row))
        for row in self.trunk:
            print("".join(row))

    def añadir_estrella(self):
        if self.estrella:
            print("Ya existe una estrella en el árbol.")
        else:
            self.estrella = True
            print("Se ha puesto la estrella en el árbol.")

    def eliminar_estrella(self):
        if not self.estrella:
            print("No existe una estrella en el árbol para quitar.")
        else:
            self.estrella = False
            print("Se ha quitado la estrella en el árbol.")

    def añadir_bolas(self):
        available = self.available()
        if len(available) < 2:
            print("No hay suficiente espacio para añadir más bolas.")
        else:
            selected = random.sample(available, 2)
            for i, j in selected:
                self.arbol[i][j] = "o"
                self.bolas.append((i, j))
            print("Se han añadido 2 bolas al árbol.")

    def eliminar_bolas(self):
        if len(self.bolas) < 2:
            print("No hay suficientes bolas para quitar.")
        else:
            selected = random.sample(self.bolas, 2)
            for i, j in selected:
                self.arbol[i][j] = "*"
                self.bolas.remove((i, j))
            print("Se han eliminado 2 bolas del árbol.")

    def añadir_luces(self):
        available = self.available()
        if len(available) < 3:
            print("No hay suficiente espacio para añadir más luces.")
        else:
            selected = random.sample(available, 3)
            for i, j in selected:
                self.arbol[i][j] = "+" if self.luces_on else "*"
                self.luces.append((i, j))
            print("Se han añadido 3 luces al árbol.")

    def eliminar_luces(self):
        if len(self.luces) < 2:
            print("No hay suficientes luces para quitar.")
        else:
            selected = random.sample(self.luces, 3)
            for i, j in selected:
                self.arbol[i][j] = "*"
                self.luces.remove((i, j))
            print("Se han eliminado 3 luces del árbol.")

    def interrumpor_luces(self, turn_on):
        if not self.luces:
            print("No hay luces en el árbol.")
 
        self.luces_on = turn_on
        for i, j in self.luces:
            self.arbol[i][j] = "+" if turn_on else "*"
        print(f"Las luces fueron {'encendidas' if turn_on else 'apagadas'}.")

    def available(self):
        available_arbol = [
            (i, j) for i in range(1, self.altura) for j in range(
                self.altura - i - 1, self.altura + i) if self.arbol[i][j] == "*"
        ]
        if not self.luces_on:
            for i, j in self.luces:
                available_arbol.remove((i, j))
        return available_arbol


altura = input("Introduce la altura del árbol: ")

if altura.isdigit() and int(altura) > 0:

    arbol = ArbolNavidad(int(altura))

    while True:

        arbol.display_arbol()

        print("\nAcciones:")
        print("1. Añadir estrella")
        print("2. Quitar estrella")
        print("3. Añadir bolas")
        print("4. Quitar bolas")
        print("5. Añadir luces")
        print("6. Quitar luces")
        print("7. Encender luces")
        print("8. Apagar luces")
        print("9. Salir")

        action = input("Selecciona una acción: ")

        match action:
            case "1":
                arbol.añadir_estrella()
            case "2":
                arbol.eliminar_estrella()
            case "3":
                arbol.añadir_bolas()
            case "4":
                arbol.eliminar_bolas()
            case "5":
                arbol.añadir_luces()
            case "6":
                arbol.eliminar_luces()
            case "7":
                arbol.interrumpor_luces(True)
            case "8":
                arbol.interrumpor_luces(False)
            case "9":
                print("¡Feliz Navidad!")
                break
            case _:
                print("Opción no válida.")

    else:
        print(f"Altura '{altura}' no válida")