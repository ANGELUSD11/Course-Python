dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(f"\nLas keys del diccionario son\n: {dictionary.keys()}")

print("\nConvirtiendo keys a lista con list")
list_keys = list(dictionary.keys())

print(f"La lista es: {list_keys}")
print(f"Posicion 1 de la lista keys: {dictionary['a']}")