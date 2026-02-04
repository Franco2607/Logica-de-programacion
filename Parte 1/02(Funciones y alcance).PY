# Simple

from itertools import count
from threading import local


def saludo():
    print("Hola")

saludo()

# Retorno

def devolver():
    return "Holaa"

print(devolver())

# Argumento

def argumento(saludo, nombre):
    print(f"{saludo}, {nombre}")

argumento(saludo=="Hola", nombre="Andrés")

# Argumento predeterminado

def predeterminado(name="python"):
    print (f"Hola, {name}")

predeterminado()

# Argumentos y retornos

def retorno(saludo, nombre):
    return f"{saludo}, {nombre}"

print(predeterminado("Franco"))
print(retorno("Hola", "Felipe"))

# Varios argumentos

# el * indica que pueden haber varios argumentos en este caso para los nombres

def varios (*nombres):
    for nombre in nombres:
        print(f"Hola, {nombre}")

varios("AI", "Franco", "Python", "Felipe")

    # Con palabras claves

def varios_key (**nombres):
    for key, value in nombres.items():
        print(f"Hola, {value}({key})")

varios_key(inteligencia="AI", apellido="Franco", lenguaje="Python", edad=17)

# Función dentro de otra función

def saludar():
    def otra():
        print("Hola mundo")
    otra()

saludar()

print(len("Hola mundo"))
print(type("Hola mundo"))
print(("Hola Mundo".lower()))

# Variables locales y globales

globalV="Mundo"

def Hola():
    local="Hola"
    print(f"{local}, {globalV}")

print(globalV)
# print(local) No se puede porque esta fuera de la funcion

def numero (text1, text2) -> int:
    contador=0
    for numeros in range(1,101):
        if numeros %3 == 0 and numeros %5 == 0:
            print(text1 + text2)
        elif numeros %3 == 0:
            print(text1)
        elif numeros %5 == 0:
            print(text2)
        else: 
            print(numeros)
            contador +=1
    return contador

print(numero("texto 1", "texto 2"))
     