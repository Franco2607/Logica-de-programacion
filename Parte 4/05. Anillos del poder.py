def primo(numero: int) -> bool:
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if (numero % i) == 0:
            return False
    return True


def distribuir_anillos(total_anillos: int):

    sauron = 1 
    total_anillos -= sauron

    anillos_distribuidos = []

#Números pares con el for
    for hombres in range(2, total_anillos, 2):
        # impares
        for elfos in range(1, total_anillos, 2):
            enanos = total_anillos - hombres - elfos
            if enanos > 0 and primo(enanos):
                anillos_distribuidos.append({
                    "Hombres": hombres,
                    "Elfos": elfos,
                    "Enanos": enanos,
                    "Sauron": sauron
                })

    if anillos_distribuidos:
        return anillos_distribuidos

    return "No es posible distribuir los anillos de poder."


try:
    total_anillos = int(
        input("Introduce el número de anillos de poder que quieres repartir: ")
    )
    anillos_distribuidos = distribuir_anillos(total_anillos)

    if isinstance(anillos_distribuidos, list):
        print("Posibles distribuciones de los anillos de poder:\n")

        for index, distribucion in enumerate(anillos_distribuidos):
            print(f"{index + 1}. {distribucion}")

        print(
            f"\nDistribución media {
                anillos_distribuidos[int(len(anillos_distribuidos) / 2)]}"
        )

    else:
        print(anillos_distribuidos)
except ValueError:
    print("Por favor, introduce un número entero de anillos.")