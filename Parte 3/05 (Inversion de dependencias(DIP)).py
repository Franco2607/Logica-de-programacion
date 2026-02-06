from abc import ABC, abstractmethod

# Los modulos de alto nivel no deben depender de los modulos de bajo nivel
# Y de lo que deben depender todos es de abstracciones y esas abstracciones no deben
#  de depender de los detalles deben depender de las implementaciones de las abstracciones
# Modulos de bajo nivel (Las tareas especificas)

# Incorrecto

class Switch:

    def encender(self):
        print("Enciende la lámpara")

    def apagar(self):
        print("Apaga la lámpara")


class Lamp:

    def __init__(self) -> None:
        self.switch = Switch()

    def operacion(self, command):
        if command == "on":
            self.switch.encender()
        elif command == "off":
            self.switch.apagar()


lamp = Lamp()
lamp.operacion("on")
lamp.operacion("off")

# Correcto


class AbstractSwitch:

    def encender(self):
        pass

    def apagar(self):
        pass


class LampSwitch(AbstractSwitch):

    def encender(self):
        print("Enciende la lámpara")

    def apagar(self):
        print("Apaga la lámpara")


class Lamp:

    def __init__(self, switch: AbstractSwitch) -> None:
        self.switch = switch

    def operacion(self, command):
        if command == "on":
            self.switch.encender()
        elif command == "off":
            self.switch.apagar()


lamp = Lamp(LampSwitch())
lamp.operacion("on")
lamp.operacion("off")

# Extra


class Notificacion(ABC):

    @abstractmethod
    def enviar(self, message: str):
        pass


class Email_Notificacion(Notificacion):
    def enviar(self, message: str):
        print(f"Enviando email con el texto: {message}")


class PUSH_Notificacion(Notificacion):
    def enviar(self, message: str):
        print(f"Enviando PUSH con el texto: {message}")


class SMS_Notificacion(Notificacion):
    def enviar(self, message: str):
        print(f"Enviando SMS con el texto: {message}")


class NotificationService:

    def __init__(self, Notificacion: Notificacion) -> None:
        self.Notificacion = Notificacion

    def notify(self, message: str):
        self.Notificacion.enviar(message)


service = NotificationService(Email_Notificacion())
# service = NotificationService(PUSH_Notificacion())
# service = NotificationService(SMS_Notificacion())
service.notify("¡Hola, notificador!")