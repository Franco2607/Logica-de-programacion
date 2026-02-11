import os

Meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]


def mostrar_menu():
    print("\nPlanificador de objetivos:")
    print("1. Añadir objetivo")
    print("2. Calcular el plan detallado")
    print("3. Guardar la planificación")
    print("4. Salir")


class Objetivo:

    def __init__(self, objetivo_name: str, cantidad: int, unidades: str, limite: int):
        self.objetivo_name = objetivo_name
        self.cantidad = cantidad
        self.unidades = unidades
        self.limite = limite


def solicitud_objetivo() -> Objetivo:

    objetivo_name = input("Meta: ")

    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad <= 0:
                print("La cantidad debe ser un número positivo.")
                continue
            break
        except:
            print("Por favor, introduce un número entero válido.")

    unidades = input("Unidades: ")

    while True:
        try:
            limite = int(input("Plazo en meses (máximo 12): "))
            if limite <= 0 or limite > len(Meses):
                print("El plazo debe ser un número entre 1 y 12 (meses).")
                continue
            break
        except:
            print("Por favor, introduce un número entre 1 y 12 (meses).")

    return Objetivo(objetivo_name, cantidad, unidades, limite)


def calcular_plan_detallado(objetivos: list[Objetivo]) -> dict:

    plan = {mes: [] for mes in range(1, len(Meses) + 1)}

    for objetivo in objetivos:
        mes_cantidad = objetivo.cantidad / objetivo.limite

        for mes in range(1, objetivo.limite + 1):
            plan[mes].append(
                Objetivo(objetivo.objetivo_name, round(mes_cantidad, 2), objetivo.unidades, objetivo.cantidad))

    return plan


def mostrar_plan_detallado(plan: dict):

    for mes in range(1, len(Meses) + 1):

        if not plan[mes]:
            # No hay objetivos en este mes
            break

        print(f"\n{Meses[mes - 1]}: ")

        for index, objetivo in enumerate(plan[mes], start=1):
            print(
                f"[ ] {index}. {objetivo.objetivo_name} ({
                    objetivo.cantidad} {objetivo.unidades}/mes). Total: {objetivo.limite}.")


def guardar_plan_detallado(plan: dict):

    file_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "plan.txt")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Plan detallado\n")

        for mes in range(1, len(Meses) + 1):

            if not plan[mes]:
                # No hay objetivos en este mes
                break

            file.write(f"\n{Meses[mes - 1]}:\n")

            for index, objetivo in enumerate(plan[mes], start=1):
                file.write(
                    f"[ ] {index}. {objetivo.objetivo_name} ({
                        objetivo.cantidad} {objetivo.unidades}/mes). Total: {objetivo.limite}.\n")

    print(f"Plan guardado con éxito en {file_path}")


objetivos = []

while True:

    mostrar_menu()

    opcion = input("Elige una opción: ")

    if opcion == "1":
        if len(objetivos) >= 10:
            print("Has alcanzado el número máximo de objetivos (10).")
        else:
            objetivo = solicitud_objetivo()
            objetivos.append(objetivo)
            print("Objetivo añadido con éxito.")

    elif opcion == "2":
        if len(objetivos) == 0:
            print("No hay objetivos añadidos.")
        else:
            plan = calcular_plan_detallado(objetivos)
            mostrar_plan_detallado(plan)

    elif opcion == "3":
        if len(objetivos) == 0:
            print("No hay objetivos para guardar.")
        else:
            plan = calcular_plan_detallado(objetivos)
            guardar_plan_detallado(plan)

    elif opcion == "4":
        print("Saliendo del planificador.")
        break
    else:
        print("Opción inválida. Elige una opción entre 1 y 4.")