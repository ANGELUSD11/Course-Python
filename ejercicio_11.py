print("\n")
#ejemplo sin validación
print("Este es un ejemplo sin validación de caracteres")
List = ["A", "B", "b", "c", "E", "E", "f"]
print(List)

element = input("Introduce el elemento que deseas eliminar: ")

for _ in List:
    if element.lower() in List:
        List.remove(element.lower())
    elif element.upper() in List:
         List.remove(element.upper())

print(f"Elemento eliminado: {List}")

#ejemplo con validación
print("\nEste es un ejemplo con validación de caracter")

l = ["A", "B", "b", "E", "E", "f"]
print(f"Lista original: {l}")
e = input("Introduce el elemento que deseas eliminar: ")

if e.lower() in l or e.upper() in l:
    while e.lower() in l:
        l.remove(e.lower())
    while e.upper() in l:
        l.remove(e.upper())
                
    print(f"Lista modificada: {l}")
else:
    print(f"{e} no se encuentra en la lista original")

#otro ejemplo sin validaciones
print("\nEste es otro ejemplo utilizando un bucle for")#NOTA: tener cuidado con los indentados
lista = ["a", "b", "B", "e", "E", "F", "G"]
print(f"Lista original: {lista}")
e = input("Introduce la letra que deseas eliminal: ")
while lista.count(e.lower()) or lista.count(e.upper()) > 0:
    for i in lista:
        if i == e.lower():
            lista.remove(e.lower())
        elif i == e.upper():
            lista.remove(e.upper())
else:
    print(f"Lista modificada: {lista}")

        

            
