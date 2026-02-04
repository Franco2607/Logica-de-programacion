# Estructuras de datos

# Listas

from typing import Literal


nombres1=["Andres","Carlos", "Felipe", "Daniel"]
print(nombres1)

#Inserta el elemento en el indice 1
nombres1.insert(1, "Juan")
#Agrega el elemento al final de la lista
nombres1.append("Pablo")
#Elimina el elemento de la lista
nombres1.remove("Felipe")
#Elimina el ultimo elemento de la lista
nombres1.pop()

print(nombres1)

# tuplas

tupla = nombres2 =("Andres","Carlos", "Felipe", "Daniel")

print(nombres2[2])

tupla = tuple(sorted(tupla))
print(tupla)

# set

nombres3 ={"Andres","Carlos", "Felipe", "Daniel"}

nombres3.add("Juan")
nombres3.remove("Andres")

print(nombres3)

# Diccionario

nombres4 = diccionario = {
    "nombre": "andres",
    "apellido": "franco",
    "edad" : 17
}
# Agregar
nombres4["sexo"] = "masculino"
# Eliminar
del nombres4["edad"]
# acceso
print(nombres4["apellido"])
# Actualizar
nombres4["edad"] = 18

print(nombres4)

# EXTRA

def agenda():

    agenda = {}

    def insert_contact():
        phone = input("Ingrese su numero de contacto: ")
        contacto=[phone]
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 10:
            agenda[name] = phone
        else:
            print("Debes introducir un numero de telefono de max 10 digitos")

    while True:
        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos")
        print("6. Salir")

        option = input("Selecciona una opción: ")

        if option == "1":
            name = input("Introduce el nombre del contacto a buscar: ")
            if name in agenda:
                print(f"El número de teléfono de {name} es {agenda[name]}.")
            else:
                print(f"El contacto {name} no existe.")
        elif option == "2":
            name = input("Introduce el nombre del contacto: ")
            insert_contact()
        elif option == "3":
            name = input("Introduce el nombre del contacto a actualizar: ")
            if name in agenda:
                insert_contact()
            else:
                print(f"El contacto {name} no existe.")
        elif option == "4":
            name = input("Introduce el nombre del contacto a a eliminar: ")
            if name in agenda:
                del agenda[name]
            else:
                print(f"El contacto {name} no existe.")
        elif option == "5":
            if agenda:
                print("Todos los contactos:")
                for nombre, telefono in agenda.items():
                    print(f"{nombre}: {telefono}")
            else:
                print("No hay contactos en la agenda.")
        elif option == "6":
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción no válida. Elige una opción del 1 al 5.")
        


agenda()