from enum import Enum

# Enum es parte de la sistanxis
class dias_sem(Enum):
    lunes = 1
    martes = 2
    miercoles = 3
    jueves = 4
    viernes = 5
    sabado = 6
    domingo = 7

def dias(numero: int):
    print(dias_sem(numero).name) #Tambien se puede el value

dias(2)

# EXTRA

class estatus(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4


class Orden:

    status = estatus.PENDIENTE

    def __init__(self, id) -> None:
        self.id = id

    def enviado(self):
        if self.status == estatus.PENDIENTE:
            self.status = estatus.ENVIADO
            self.display_status()
        else:
            print("El pedido ya ha sido enviado o cancelado")

    def entregado(self):
        if self.status == estatus.ENVIADO:
            self.status = estatus.ENTREGADO
            self.display_status()
        else:
            print("El pedido necesita ser enviado antes de entregarse.")

    def cancelado(self):
        if self.status != estatus.ENTREGADO:
            self.status = estatus.CANCELADO
            self.display_status()
        else:
            print("El pedido no se puede cancelar ya que ya se ha entregado.")

    def display_status(self):
        print(f"El estado del pedido {self.id} es {self.status.name}")


Orden_1 = Orden(1)
Orden_1.display_status()
Orden_1.entregado()
Orden_1.enviado()
Orden_1.entregado()
Orden_1.cancelado()