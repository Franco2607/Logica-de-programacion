import random
import time
import threading

# threading sirve para implementar multihilo (multithreading), permitiendo que un programa ejecute múltiples tareas concurrentemente (al mismo tiempo) dentro de un mismo proceso

# Es una funcion que se le pasa como argumento o parametro a otra función
# funciones pasadas como argumentos a otras funciones para ser ejecutadas posteriormente, usualmente tras finalizar una tarea específica, un evento o una operación asíncrona

def saludo(name:  str, callback):
    callback(name)

def llamada(name: str):
    print(f"Hola, {name}!")

saludo("Franco", llamada)

# EXTRA

def order_process(dish_name: str, confirm_callback, ready_callback, delivered_callback):
    def process():
        confirm_callback(dish_name)
        time.sleep(random.randint(1, 10))
        ready_callback(dish_name)
        time.sleep(random.randint(1, 10))
        delivered_callback(dish_name)

    threading.Thread(target=process).start()


def confirm_order(dish_name: str):
    print(f"Tu pedido {dish_name} ha sido confirmado.")


def order_ready(dish_name: str):
    print(f"Tu pedido {dish_name} está listo.")


def order_delivered(dish_name: str):
    print(f"Tu pedido {dish_name} ha sido entregado.")


order_process("Pizza Barbacoa", confirm_order, order_ready, order_delivered)
order_process("Pizza 4 Quesos", confirm_order, order_ready, order_delivered)
order_process("Pizza Margarita", confirm_order, order_ready, order_delivered)
order_process("Pizza con Piña", confirm_order, order_ready, order_delivered)