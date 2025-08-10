print("Lista original")

letters = ["b", "d", "f", "g"]
print(f"Lista: {letters}")

print("\nInsertando 'a' en posición 0")
letters.insert(0, "a")
print(f"Lista: {letters}")

print("\nInsertando 'c' en posición 2")
letters.insert(2, "c")
print(f"Lista: {letters}")

print("\nInsertando 'e' en posición 4")
letters.insert(4, "e")
print(f"Lista: {letters}")

print("\nInsertando 'z' en posición 100")
letters.insert(100, "z")
print(f"Lista: {letters}")

print("Lista original")
letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
print("Lista modificada")
letras_1 = ["a", "c", "f", "h"]
print(letras_1)

print("¿Qué elementos hacen falta en la lista modificada?")

for letter in letras:
    if letter not in letras_1:
        add_letter = input(f"¿Desea agregar la letra {letter} a la lista modificada? [S/N]: ")
        if add_letter.lower() == "s":
            letras_1.append(letter)
print(f"Lista modificada: {letras_1} ")

print("Lista original")
letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
print("Lista modificada")
letras_1 = ["a", "c", "f", "h"]
print(letras_1)

missing_letters = []

for letter in letras:
    if letter not in letras_1:
        missing_letters.append(letter)
print(f"Letras faltantes en la lista modificada: {missing_letters} ")

# el usuario agrega las letras faltantes
letras_1 += input("Escriba las letras faltantes separadas por comas: ").split(",")

print(f"Lista modificada: {letras_1} ")
