laberinto = [
    ["🐭", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
    ["⬜️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️"],
    ["⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️"],
    ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
    ["⬛️", "⬜️", "⬛️", "⬜️", "⬛️", "⬛️"],
    ["⬛️", "⬜️", "⬛️", "⬜️", "⬜️", "🚪"]
]

 
def Mickey_Maze():
    for fila in laberinto:
        print("".join(fila))
    print()


mickey = [0, 0]


while True:

    Mickey_Maze()

    print("¿Hacia dónde se mueve Mickey?")
    print("[w] arriba")
    print("[s] abajo")
    print("[a] izquierda")
    print("[d] derecha")
    direccion = input("Dirección: ")

    fila_actual, columna_actual = mickey
    nueva_fila, nueva_columna = fila_actual, columna_actual

    match direccion:
        case "w":
            nueva_fila = fila_actual - 1
        case "s":
            nueva_fila = fila_actual + 1
        case "a":
            nueva_columna = columna_actual - 1
        case "d":
            nueva_columna = columna_actual + 1
        case _:
            print("Dirección no válida.\n")
            continue

    if nueva_fila < 0 or nueva_fila > 5 or nueva_columna < 0 or nueva_columna > 5:
        print("No puedes desplazarte fuera del laberinto.\n")
        continue
    else:
        if laberinto[nueva_fila][nueva_columna] == "⬛️":
            print("¡En esa dirección hay un obstáculo!\n")
            continue
        elif laberinto[nueva_fila][nueva_columna] == "🚪":
            print("¡Has encontrado la salida!")
            laberinto[fila_actual][columna_actual] = "⬜️"
            laberinto[nueva_fila][nueva_columna] = "🐭"
            Mickey_Maze()
            break
        else:
            laberinto[fila_actual][columna_actual] = "⬜️"
            laberinto[nueva_fila][nueva_columna] = "🐭" 
            mickey = [nueva_fila, nueva_columna]