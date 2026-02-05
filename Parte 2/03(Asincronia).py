import datetime
import time
import asyncio

# La asíncronia es: poder de ejecución de un proceso en segundo plano

async def tarea(name: str, duration: int):
    print(f"Tarea: {name}, Duración: {duration}s, inicio: {datetime.datetime.now()}")
    await asyncio.sleep(duration)
    print(f"Tarea: {name}, Fin: {datetime.datetime.now()}")

asyncio.run(tarea("1", 2))

# EXTRA 
# "gather" Una tarea que va a acabar en un futuro

async def async_tarea():
    await asyncio.gather(tarea("C", 3),tarea("B", 2),tarea("A", 1))
    await tarea("D", 1)

asyncio.run(async_tarea())

