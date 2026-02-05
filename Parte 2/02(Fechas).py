from datetime import datetime, date, timedelta

actual = datetime.now()

cumple = datetime(2008, 7, 26, 12, 0, 0)

print(actual)
print(cumple)

edad = actual - cumple

print(type(edad))

# "//" es para hacer la division entera

print(f"Tengo {edad.days // 365} años")


# EXTRA

# Dia, mes y año

print(cumple.strftime("%d/%m/%y"))
print(cumple.strftime("%d/%m/%Y"))

# Horas, minuto y segundos

print(cumple.strftime("%H:%M:%S"))

# Dia del año

print(cumple.strftime("%j"))

# Dia de la semana

print(cumple.strftime("%A"))

# Nombre del mes

print(cumple.strftime("%h"))
print(cumple.strftime("%B"))

# Representación por defecto del locale

print(cumple.strftime("%c"))
print(cumple.strftime("%x"))
print(cumple.strftime("%X"))

# AM/PM

print(cumple.strftime("%p"))


# cumple1 = datetime(2008, 7, 26, 12, 0, 0)