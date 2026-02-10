from datetime import datetime, timedelta

# Reto 1

año_de_creacion = 1939
año_aniversario = año_de_creacion + 85

aniversario_batman_fecha = []

while año_aniversario <= año_de_creacion + 100:

    septiembre = datetime(año_aniversario, 9, 1)

    primer_sabado = 5 - septiembre.weekday() if septiembre.weekday() <= 5 else 12 - \
        septiembre.weekday()

    tercer_sabado = septiembre + timedelta(days=primer_sabado + 14)

    aniversario_batman_fecha.append(
        (
            año_aniversario,
            año_aniversario - año_de_creacion,
            tercer_sabado.strftime("%d-%m-%Y")
        )
    )

    año_aniversario += 1

for year, aniversario, batman_day in aniversario_batman_fecha:
    print(f"Batman day {year} ({aniversario} aniversario): {batman_day}")

# Reto 2


def sum_alert_cuadricula(sensores, center_x, center_y) -> int:

    total = 0

    for x in range(center_x - 1, center_x + 2):
        for y in range(center_y - 1, center_y + 2):
            for sensor in sensores:
                if sensor[0] == x and sensor[1] == y:
                    total += sensor[2]

    return total


def sistema_seguridad_baticueva(sensores):

    nivel_max_alerta = 0
    cordenada_max_alerta = (0, 0)

    for x in range(1, 19):
        for y in range(1, 19):
            nivel_de_alerta = sum_alert_cuadricula(sensores, x, y)
            if nivel_de_alerta > nivel_max_alerta:
                nivel_max_alerta = nivel_de_alerta
                cordenada_max_alerta = (x, y)
# "abs" Valor absoluto
    distancia = abs(cordenada_max_alerta[0]) + abs(cordenada_max_alerta[1])
    activar_protocolo = nivel_max_alerta > 20

    return cordenada_max_alerta, nivel_max_alerta, distancia, activar_protocolo


sensores = [
    (3, 4, 8),
    (5, 4, 10),
    (3, 3, 8),
    (8, 10, 12),
    (10, 10, 7),
    (11, 10, 7),
    (12, 15, 6)
]

result = sistema_seguridad_baticueva(sensores)
print(f"Centro cuadrícula más amenazada: {result[0]}.")
print(f"Máximo nivel de alerta: {result[1]}.")
print(f"Distancia a la Batcueva: {result[2]}.")
print(f"Activar protocolo de seguridad: {"Sí" if result[3] else "No"}.")