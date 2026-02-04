# Se importa OS

import os

# open ("Franco8126.txt", "w")

# Fichero = "Franco8126.txt"

# "w" es para escribir en el archivo
# "r" es para leer el archivo
# "a" es para agregar al archivo (append)
# "x" es para crear el archivo
# "b" es para binario
# "t" es para texto
# "+" es para lectura y escritura
# "U" es para universal newlines

# with open(Fichero, "w") as file:
#     file.write("Andres Felipe Franco\n")
#     file.write("17\n")
#     file.write("Python\n")

# with open(Fichero, "r") as file:
#     print(file.read())

# "os.remove" es para eliminar el archivo

# os.remove(Fichero)

# EXTRA

nom_archivo = "Franco.txt"

open(nom_archivo, "a")

while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")

    option = input("Selecciona una opción: ")

    if option == "1":
        nombre = input("Nombre del producto a comprar: ")
        cantidad = input("Cantidad del producto: ")
        precio = input("Precio del producto: ")
        with open(nom_archivo, "a") as file:
            file.write(f"{nombre}, {cantidad}, {precio}\n")
    elif option == "2":
        nombre = input("Nombre: ")
        with open(nom_archivo, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == nombre:
                    print(line)
                    break
    elif option == "3":
        nombre = input("Nombre: ")
        cantidad = input("Cantidad: ")
        precio = input("Precio: ")
        with open(nom_archivo, "r") as file:
            lines = file.readlines()
        with open(nom_archivo, "w") as file:
            for line in lines:
                if line.split(", ")[0] == nombre:
                    file.write(f"{nombre}, {cantidad}, {precio}\n")
                else:
                    file.write(line)
    elif option == "4":
        nombre = input("Nombre: ")
        with open(nom_archivo, "r") as file:
            lines = file.readlines()
        with open(nom_archivo, "w") as file:
            for line in lines:
                if line.split(", ")[0] != nombre:
                    file.write(line)
    elif option == "5":
        with open(nom_archivo, "r") as file:
            print(file.read())
    elif option == "6":
        total = 0
        with open(nom_archivo, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                cantidad = int(components[1])
                precio = float(components[2])
                total += cantidad * precio
        print(f"El total a pagar es: {total}")
    elif option == "7":
        nombre = input("Nombre: ")
        total = 0
        with open(nom_archivo, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                if components[0] == nombre:
                    cantidad = int(components[1])
                    precio = float(components[2])
                    total += cantidad * precio
                    break
        print(total)
    elif option == "8":
        os.remove(nom_archivo)
        break
    else:
        print("Selecciona una de las opciones disponibles.")