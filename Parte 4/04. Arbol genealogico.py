class persona:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.pareja = None
        self.niños = []
        self.tiene_padres = False

    def añadir_pareja(self, pareja):
        if self.pareja is not None:
            print(f"{self.name} ya tiene una pareja: {self.pareja.name}.")
        else:
            self.pareja = pareja
            pareja.pareja = self
            print(f"{self.name} es pareja de {pareja.name}.")

    def añadir_hijo(self, niño):
        if niño not in self.niños:
            self.niños.append(niño)
            print(f"{self.name} ha tenido un hijo: {niño.name}")
        else:
            print(f"{niño.name} ya es hijo de {self.name}.")


class Arbol_genealogico:

    def __init__(self):
        self.personas = {}

    def añadir_persona(self, id, name):
        if id in self.personas:
            print(f"La persona con ID: {id} ya existe.")
        else:
            personas = persona(id, name)
            self.personas[id] = personas
            print(
                f"La persona con nombre {name} [ID: {id}] ha sido añadida al árbol.")

    def eliminar_persona(self, id):
        if id in self.personas:
            persona = self.personas[id]
            del self.personas[id]
            print(
                f"La personaa con nombre {persona.name} [ID: {id}] ha sido eliminada del árbol.")
        else:
            print(f"La persona con ID: {id} no existe en el árbol.")

    def establecer_pareja(self, id1, id2):
        if id1 in self.personas and id2 in self.personas:
            persona1 = self.personas[id1]
            persona2 = self.personas[id2]
            persona1.añadir_pareja(persona2)
        else:
            print("Algún ID no existe en el árbol.")

    def añadir_hijo(self, padres_id, niño_id):
        if padres_id in self.personas and niño_id in self.personas:
            if padres_id == niño_id:
                print("Los ID no pueden ser iguales a la hora de asignar un hijo.")
            else:
                parent = self.personas[padres_id]
                if parent.pareja is None:
                    print(f"Se necesita una pareja para poder tener un hijo.")
                else:
                    niño = self.personas[niño_id]
                    if niño.tiene_padres:
                        print(
                            f"{niño.name} [ID: {niño.id}] ya tiene padres.")
                    else:
                        niño.tiene_padres = True
                        parent.añadir_hijo(niño)
                        parent.pareja.añadir_hijo(niño)
        else:
            print("Algún ID no existe en el árbol.")

    def imprimir_arbol(self):

        visited = set()

        def imprimir_persona(persona, level=0):

            if persona.id in visited:
                return

            visited.add(persona.id)

            indentar = "\t" * level

            print(f"{indentar} - {persona.name} [ID: {persona.id}]")

            if persona.pareja:
                visited.add(persona.pareja.id)
                print(
                    f"{indentar}   Pareja: {persona.pareja.name} [ID: {persona.pareja.id}]")

            if persona.niños:
                print(f"{indentar}   Hijos:")
                for niño in persona.niños:
                    imprimir_persona(niño, level + 1)

        for persona in self.personas.values():
            is_niño = persona.tiene_padres
            if not is_niño:
                imprimir_persona(persona)


tree = Arbol_genealogico()

tree.añadir_persona(1, "Jocelyn")
tree.añadir_persona(2, "Aemon")

tree.establecer_pareja(1, 2)

tree.añadir_persona(3, "Rhaenys")

tree.añadir_hijo(1, 3)

tree.añadir_persona(4, "Corlys")

tree.establecer_pareja(3, 4)

tree.añadir_persona(5, "Laena")
tree.añadir_persona(6, "Laenor")

tree.añadir_hijo(3, 5)
tree.añadir_hijo(3, 6)

tree.añadir_persona(7, "Baelon")
tree.añadir_persona(8, "Alyssa")

tree.establecer_pareja(7, 8)

tree.añadir_persona(9, "Viserys I")
tree.añadir_persona(10, "Daemon")

tree.añadir_hijo(7, 9)
tree.añadir_hijo(8, 10)

tree.añadir_persona(11, "Aemma")

tree.establecer_pareja(9, 11)

tree.añadir_persona(12, "Rhaenyra")

tree.añadir_hijo(9, 12)

tree.establecer_pareja(10, 12)

tree.añadir_persona(13, "Aegon")
tree.añadir_persona(14, "Viserys")

tree.añadir_hijo(12, 13)
tree.añadir_hijo(12, 14)

tree.imprimir_arbol()