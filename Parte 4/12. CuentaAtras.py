import datetime
import time
import os
import threading


def cuenta_atrás(fecha_obj):

    while True:

        fecha_ahora_utc = datetime.datetime.now(datetime.timezone.utc)

        tiempo_restante = fecha_obj - fecha_ahora_utc

        if tiempo_restante.total_seconds() <= 0:
            print("\n¡Cuenta atrás finalizada!")
            break

        days, seconds = divmod(tiempo_restante.total_seconds(), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        os.system("clear")

        print(
            f"Tiempo restante: {int(days)} días, {int(hours)} horas, {int(minutes)} minutos, {int(seconds)} segundos")

        time.sleep(1)


fecha_local = datetime.datetime(2026, 7, 26, 12, 12, 12)
fecha_local = fecha_local.replace(
    tzinfo=datetime.datetime.now().astimezone().tzinfo)

fecha_obj_utc = fecha_local.astimezone(datetime.timezone.utc)

hilo_cuenta_regresiva = threading.Thread(target=cuenta_atrás, args=(fecha_obj_utc,))
hilo_cuenta_regresiva.start()
hilo_cuenta_regresiva.join()
