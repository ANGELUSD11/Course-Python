print("\nEste es un ejemplo con validación de caracter")

l = ["A", "B", "b", "E", "E", "f"]
print(f"Lista original: {l}")
e = input("Introduce el elemento que deseas eliminar: ")

if e in [i.lower() for i in l] or e in [i.upper() for i in l]:
    l = [i for i in l if i.lower() != e.lower()]
    print(f"Lista modificada: {l}")
else:
    print(f"{e} no se encuentra en la lista original")
