numbers = []
long_list = int(input("cuantos numeros enteros contendra la lista: "))

for _ in range(long_list):
    numbers.append(int(input("introduce un numero entero: ")))

print(f"\nLista: {numbers} \nLa suma total de los elementos es: {sum(numbers)}")
