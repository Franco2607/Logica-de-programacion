# La libreria csv se usa para poder trabajar con csv

import csv
import os
import random



def leer_data_csv() -> list:

# dirname es la dirección del fichero
    direccion_archivo = os.path.dirname(os.path.abspath(__file__))
    archivo_csv = f"{direccion_archivo}/subs.csv"

    data = []

    with open(archivo_csv, mode="r")   as file:
        # "DictReader"Genera un objeto que permite la lectura de cada una de las filas creando un dic
        reader = csv.DictReader(file) 
        for fila in reader:
            if fila["status"] == "activo":
                data.append(fila)

    return data


def seleccionar_ganadores(data: list) -> list:

    if len(data) < 3:
        raise ValueError("El número de elementos debe ser mínimo 3.")

    return random.sample(data, 3)


def mostrar_ganadores(ganadores):
    premios = ["Suscripción", "Descuento", "Libro"]
    for ganador, premio in zip(ganadores, premios):
        print(f"{premio}: {ganador["email"]} (ID: {ganador["id"]})")


try:
    data = leer_data_csv()
    ganadores = seleccionar_ganadores(data)
    mostrar_ganadores(ganadores)
except Exception as e:
    print(e)