print("Las tablas de multiplicar :D")

num = int(input("¿Qué tabla de multiplicar quieres ver?: "))

print(f"\nLa tabla del {num} es: ")
for indice in range(11):
    print(f"{num} x {indice} = {num * indice}")

print("Fin del programa")


