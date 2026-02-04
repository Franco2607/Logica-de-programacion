#Aritmeticos 
Suma = 5+5
Resta = 15-5
Multi = 2*5
Divi = 10/2

print(Suma)
print(Resta)
print(Multi)
print(Divi)

# Comparación

Five = 5
Dife = 7 != 5
Mayor = 10>5
Menor = 5<10

print(Five)
print(Dife)
print(Mayor)
print(Menor)

# Lógicos

V= True

AND = Suma and Resta == 10
OR = Multi or Divi == 10
NOT = not Divi

print(AND)
print(OR)
print(NOT)

# Asignación

contadorS=1
contadorR=1
contadorM=2
contadorD=4

six = 6
contadorS += 1
contadorR -= 1
contadorM *= 2
contadorD /= 2

print(contadorS)
print(contadorR)
print(contadorM)
print(contadorD)

# Identidad

mi_numero = 1234
print(f"Mi numero es: {mi_numero}")

# Bit
a = 10 #1010
b = 3 #0011

# Estructuras de control

# Condicionales

age= int(input("Ingrese su edad: "))

if 6> age >= 0:
    print("Primera infancia")
elif 12> age >= 6:
    print("Infancia")
elif 19> age >= 12:
    print("Adolescencia")
else:
    print("Eres mayor de edad")

# Repetición

for i in range (10,56):
    print(i)

contador = 0

while contador < 3:
    contador+=1
    print(f"Intento {contador}")

# Contraseña

usu = "ADMIN"
contra = 123

print("Iniciar de sesion")

for i in range(3):
    usuario = str(input("Ingrese el usuario: "))
    contraseña = int(input("Ingrese la contraseña: "))
    if usuario == usu and contraseña == contra:
        print("Iniciaste sesion correctamente")
        break  
    else:
        print("Usuario o contraseña incorrecta")

#Excepciones

try:
    result= 10/0
except ZeroDivisionError:
    print("Error, ¡No se puede dividir por cero!")

# Dificultad extra

for num in range(10,56):
    if num%2 == 0 and num != 16 and num %3 !=0:
        print(num)
