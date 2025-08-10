dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(f"\nLos items del diccionario son\n {dictionary.items()}")

print("\nConvirtiendo items a lista con list")

list_items = list(dictionary.items())

print(f"La lista es: {list_items}")
print(f"Posicion 1 de la lista Items: {list_items[1]}")
