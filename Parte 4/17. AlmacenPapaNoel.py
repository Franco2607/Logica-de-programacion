import random

letras = ["A", "B", "C"]
numeros = ["1", "2", "3"]
elementos_contra = letras + numeros


def generar_contra() -> str:
    return "".join(random.sample(elementos_contra, 6))


contra_secreta = generar_contra()
intentos = 1

print("Adivina la contraseña del almacén de Papá Noel.")

while intentos <= 10:

    print(f"Intento: {intentos}")

    contra = input("Introduce la contraseña: ").upper()

    if len(contra) != 6:
        print("Error: La contraseña debe tener 4 caracteres.")
        continue
    if not all(character in elementos_contra for character in contra):
        print(f"Error: Sólo se permiten los caracteres {elementos_contra}.")
        continue

    if contra == contra_secreta:
        print("¡Contraseña correcta! Has descifrado el código del almacén. Feliz Navidad.")
        break

    intentos += 1

    if intentos > 10:
        print("Lo siento, los 10 intentos para descifrar el código han finalizado.")
        print("Papá Noel no ha podido entregar los regalos.")
    else:
        for index, character in enumerate(contra):
            if character == contra_secreta[index]:
                print(f"{character}: Correcto")
            elif character in contra_secreta:
                print(f"{character}: Presente")
            else:
                print(f"{character}: Incorrecto")