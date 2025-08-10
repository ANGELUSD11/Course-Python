palabra = input("introduce una palabra: ")
num_int = int(input("introduce un numero entero: "))
num_float = float(input("introduce un numero flotante: "))
num_complex = complex(input("introduce un numero complejo: "))

print("string: ", palabra)
print("entero: ", num_int)
print("flotante: ", num_float)
print("complejo: ", num_complex)

nombre = input("introduce un nombre de usuario: ")
print("hola " + ", vamos a realizar una suma.")
num_uno = int(input("por favor introduce un valor: "))
num_dos = int(input("por favor introduce el segundo valor: "))


resultado = num_uno + num_dos

print(nombre + " el resultado de la suma es: ", resultado)

nombre = input("introduce un nombre de usuario: ")
print("hola " + ", vamos a realizar una comparacion.")
num_uno = bool(input("por favor introduce un valor: "))
num_dos = bool(input("por favor introduce el segundo valor: "))

resultado = num_uno == num_dos
print(nombre + " el resultado de la comparación es: ", resultado)
