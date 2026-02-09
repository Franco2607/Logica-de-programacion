import random
import time

vida_deadpool = int(input("Introduce la vida de Deadpool: "))
vida_wolverine = int(input("Introduce la vida de Wolverine: "))

turno = 0
regeneracion = False

while vida_deadpool > 0 and vida_wolverine > 0:

    turno += 1
    print(f"\nTurno {turno}")

    # Deadpool ataca a Wolverine

    if regeneracion:
        print("Deadpool se está regenerando y no ataca.")
        regeneracion = False
    elif random.random() > 0.2:
        daño_deadpool = random.randint(10, 100)
        print(f"Deadpool ataca a Wolverine con {daño_deadpool} de daño.")
        if daño_deadpool == 100:
            regeneracion = True
            print(
                "¡Golpe crítico de Deadpool! Wolverine no atacará en el siguiente turno ya que tiene que regenerarse.")

        vida_wolverine -= daño_deadpool

        if vida_wolverine <= 0:
            print(f"La vida de Wolverine ha llegado a cero.")
            break
        else:
            print(f"Vida restante de Wolverine: {vida_wolverine}")
    else:
        print("¡Wolverine esquiva el ataque de Deadpool!")

    # Wolverine ataca a Deadpool

    if regeneracion:
        print("Wolverine se está regenerando y no ataca.")
        regeneracion = False
    elif random.random() > 0.25:
        daño_wolverine = random.randint(10, 120)
        print(f"Wolverine ataca a Deadpool con {daño_wolverine} de daño.")
        if daño_wolverine == 120:
            regeneracion = True
            print(
                "¡Golpe crítico de Wolverine! Deadpool no atacará en el siguiente turno ya que tiene que regenerarse.")

        vida_deadpool -= daño_wolverine

        if vida_deadpool <= 0:
            print(f"La vida de Deadpool ha llegado a cero.")
            break
        else:
            print(f"Vida restante de Deadpool: {vida_deadpool}")
    else:
        print("¡Deadpool esquiva el ataque de Wolverine!")

    time.sleep(1)

if vida_deadpool > 0:
    print(f"Deadpool gana la batalla con {vida_deadpool} de vida restante.")
else:
    print(
        f"Wolverine gana la batalla con {vida_wolverine} de vida restante.")