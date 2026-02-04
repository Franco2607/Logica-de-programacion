text = "hola mundo"
print(text)

text[0]
print(text[0:4])
print(len(text))

print(text.upper())
print(text.lower())
print(text.title())
print(text.replace("hola", "chao"))

concatenar="Hola" + " " + "Mundo"
print(concatenar)
repetir="ja"*3
print(repetir)

print("hola" in text)
print(text.isnumeric())
print(text.isalpha())
print(text.find("mundo"))

# EXTRA

def solucion(palabra1: str, palabra2: str):

    # Palíndromos
    print(f"¿{palabra1} es un palíndromo?: {palabra1 == palabra1[::-1]}")
    print(f"¿{palabra2} es un palíndromo?: {palabra2 == palabra2[::-1]}")

    # Anagramas
    print(f"¿{palabra1} es anagrama de {palabra2}?: {sorted(palabra1) == sorted(palabra2)}")

    # Isogramas

    def isogram(palabra: str) -> bool:

        PalabraD = dict() 
        for character in palabra:
            PalabraD[character] = PalabraD.get(character, 0) + 1

        isogram = True
        values = list(PalabraD.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break

        return isogram

    print(f"¿{palabra1} es un isograma?: {isogram(palabra1)}")
    print(f"¿{palabra2} es un isograma?: {isogram(palabra2)}")


solucion("radar", "amor")
