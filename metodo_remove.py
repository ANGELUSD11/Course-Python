#metodo remove()

vocales = ["a", "e", "i", "o", "u"]
print(f"{vocales} \nElemento a eliminar: i")
vocales.remove("i")
print(vocales)

vocales = ["a", "e", "i", "o", "u"]
print(f"\n{vocales} \nElemento a eliminar: o")
vocales.remove("o")
print(vocales)

vocales = ["a", "e", "i", "o", "i"]
print(f"\n{vocales} \nElemento a eliminar: i")
vocales.remove("i")
print(vocales)

vocales = ["a", "e", "i", "o", "i"]
print(f"\n{vocales} \nElemento a eliminar: i")
vocales.remove("i")
print(vocales)

vocales = ["a", "e", "i", "o", "i"]
print(f"respaldo de la lista original: {vocales}")
print(f"\n{vocales} \nElementos a eliminar: i")
vocales = [v for v in vocales if v != "i"]
print(vocales)

vocales = ["a", "o", "i", "i", "o"]
print(f"\n{vocales} \nEliminar elementos repetidos")

for i in vocales:
    if vocales.count(i) > 1:
        vocales.remove(i)

print(vocales)

vocales = ["a", "o", "i", "i", "o"]
print(f"\n{vocales} \nElementos a eliminar: i repetidas")

for v in vocales:
    if vocales.count("i") > 1:
        vocales.remove("1")

print(vocales)
