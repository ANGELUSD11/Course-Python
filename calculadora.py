print("Calculadora ANGELUS, \n")

print("1. suma")
print("2. resta")
print("3. mutiplicación")
print("4. división")
print("5. div entera")
print("6. potencia")
print("7. módulo \n")

numero = int(input("seleccione una opción: "))

if numero == 1:
    print("elegiste suma")
    numero = int(input("escribe el primer numero: "))
    numero += int(input("escribe el segundo numero: "))
    print("el resultado de la suma es:", numero)

elif numero == 2:
    print("elegiste resta")
    numero = int(input("escribe el primer numero: "))
    numero -= int(input("escribe el segundo numero: "))
    print("el resultado de la resta es:", numero)

elif numero == 3:
    print("elegiste multiplicación")
    numero = int(input("escribe el primer numero: "))
    numero *= int(input("escribe el segundo numero: "))
    print("el resultado de la multiplicación es:", numero)

elif numero == 4:
    print("elegiste división")
    numero = int(input("escribe el primer numero: "))
    numero /= int(input("escribe el segundo numero: "))
    print("el resultado de la división es:", numero)

elif numero == 5:
    print("elegiste división entera")
    numero = int(input("escribe el primer numero: "))
    numero //= int(input("escribe el segundo numero: "))
    print("el resultado de la división entera es:", numero)

elif numero == 6:
    print("elegiste potencia")
    numero = int(input("escribe el primer numero: "))
    numero **= int(input("escribe el segundo numero: "))
    print("el resultado de la potencia es:", numero)

elif numero == 7:
    print("elegiste módulo")
    numero = int(input("escribe el primer numero: "))
    numero %= int(input("escribe el segundo numero: "))
    print("el resultado del módulo es:", numero)

else:
    print("opción no disponible")
