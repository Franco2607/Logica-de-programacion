from functools import reduce
from datetime import datetime

# Son funciones que pueden recibir funciones como parametros/argumentos y devolver funciones como resultado

# Funcion como argumento

import numbers


def aplicar_func (func, x):
    return func(x)

x = aplicar_func(len, "Franco")
print(x)

# Retorno de funcion

def aplicar_multiplayer(n):
    def multiplayer(x):
        return x * n
    return multiplayer

multiplayer = aplicar_multiplayer(2)
print(multiplayer(5))
print(aplicar_multiplayer(3)(2))

#  Sistema

numbers = [5, 3, 2, 4, 1]

# map() le pasamos una lista (argumento) y una funcion y devuelve una nueva lista que contiene el resultado de aplicar esa funcion a todos los elementos de esa lista

def aplicar_doble(n):
    return n * 2

print(list(map(aplicar_doble, numbers))) 

# filter()

def par(n):
    return n % 2

print(list(filter(par, numbers)))

# sorted() Ordena

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, key=lambda x: -x))

# reduce()

def suma(x, y): 
    return x + y

print(reduce(suma, numbers))


# EXTRA 

estudiantes = [
    {"name": "Andres", "cumple": "26-07-2008", "notas": [10, 9, 10, 8.5, 9.5]},
    {"name": "Juan", "cumple": "29-10-2002", "notas": [8, 7, 4, 4, 8]},
    {"name": "Carlos", "cumple": "16-09-2004", "notas": [4, 6.4, 10, 4, 10]}
]


def media(notas):
    return sum(notas) / len(notas)

# Promedio

print(
    list(map(lambda estudiante: {
        "name": estudiante["name"],
        "average": media(estudiante["notas"])}, estudiantes)
    )
)

# Mejores

print(
    list(
        map(lambda estudiante:
            estudiante["name"],
            filter(lambda estudiante: media(estudiante["notas"]) >= 9, estudiantes)
            )
    )
)

# Menor a mayor

print(sorted(estudiantes, key=lambda estudiante: datetime.strptime(
    estudiante["cumple"], "%d-%m-%Y"), reverse=True))

# Calificacion mas alta

print(max(map(lambda estudiante: max(estudiante["notas"]), estudiantes)))