from abc import ABC, abstractmethod

# Establece que una clase no deberia de estar obligada a implemetar interfaces 
# que no utiliza
# Este principio fomenta es que se diseñen interfaces especificas para cada tipo de lógica

# Incorrecto


class Interface_trabajador(ABC):

    @abstractmethod
    def Trabajar(self):
        pass

    @abstractmethod
    def Comer(self):
        pass


class Humano(Interface_trabajador):

    def Trabajar(self):
        print("Trabajando")

    def Comer(self):
        print("Comiendo")


class Robot(Interface_trabajador):

    def Trabajar(self):
        print("Trabajando")

    def Comer(self):
        # Los robots no Comen

        pass


Humano = Humano()
Humano.Trabajar()
Humano.Comer()

robot = Robot()
robot.Trabajar()
robot.Comer()  # error

# Con ISP


class Interface_trabajador(ABC):

    @abstractmethod
    def Trabajar(self):
        pass


class ComerInterface(ABC):

    @abstractmethod
    def Comer(self):
        pass


class Humano(Interface_trabajador, ComerInterface):

    def Trabajar(self):
        print("Trabajando")

    def Comer(self): 
        print("Comiendo")


class Robot(Interface_trabajador):

    def Trabajar(self):
        print("Trabajando")


Humano = Humano()
Humano.Trabajar()
Humano.Comer()

robot = Robot()
robot.Trabajar()


# Extra



class Imprimir_interface(ABC):

    @abstractmethod
    def imprimir(self, document: str):
        pass


class Color_interface(ABC):

    @abstractmethod
    def imprimir_color(self, document: str):
        pass


class Escaner_interface(ABC):

    @abstractmethod
    def scan(self, document: str) -> str:
        pass


class Fax_interface(ABC):

    @abstractmethod
    def send_fax(self, document: str):
        pass


class Printer(Imprimir_interface):
    def imprimir(self, document: str):
        print(f"Imprimiendo en blanco y negro el documento {document}.")


class ColorPrinter(Color_interface):
    def imprimir_color(self, document: str):
        print(f"Imprimiendo a color el documento {document}.")


class Impresora_multi(Imprimir_interface, Color_interface, Escaner_interface, Fax_interface):
    def imprimir(self, document: str):
        print(f"Imprimiendo en blanco y negro el documento {document}.")

    def imprimir_color(self, document: str):
        print(f"Imprimiendo a color el documento {document}.")

    def scan(self, document: str) -> str:
        print(f"Escaneando el documento {document}.")
        return f"Documento {document} escaneado."

    def send_fax(self, document: str):
        print(f"Enviando por fax el documento {document}.")


def test_printers():

    printer = Printer()
    color_printer = ColorPrinter()
    multifunction_printer = Impresora_multi()

    printer.imprimir("doc.pdf")
    color_printer.imprimir_color("doc.pdf")
    multifunction_printer.imprimir("doc.pdf")
    multifunction_printer.imprimir_color("doc.pdf")
    multifunction_printer.scan("doc.pdf")
    multifunction_printer.send_fax("doc.pdf")


test_printers()