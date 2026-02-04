for i in range (1,11):
    print (i)

contador=1

while contador<11:
    print (contador)
    contador+=1

def contador1(i = 1) -> int:
    if i <= 10:
        print(i)
        contador1(i + 1)

contador1(1)

# EXTRA 

for e in [1, 2, 3, 4]:
    print(e)

for e in {1, 2, 3, 4}:
    print(e)

for e in (1, 2, 3, 4):
    print(e)

# Acá se puede poner .values (a,b,c,d) y .keys
for e in {1: "a", 2: "b", 3: "c", 4: "d"}:
    print(e)

print(*[i for i in range(1,11)], sep="\n") 

for c in "python":
    print(c)

for e in reversed([1, 2, 3, 4]):
    print(e)

for e in sorted (["F", "r", "a", "n", "c", "o"]):
    print(e) 

for e in enumerate(sorted (["F", "r", "a", "n", "c", "o"])):
    print(f"Indice: {i}, valor: {e}") 