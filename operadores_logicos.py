#and identifica que todas las condiciones se cumplan
#or identifica que alguna de las condiciones se cumpla
#not niega la condición

#conjuncion

print("conjuncion (and)")

num_uno = int(input("escribe un numero mayor a 2 y menor a 5: "))

if num_uno > 2 and num_uno < 5:
    print("el numero ", num_uno, "cumple con la condicion. :D \n")
else:
    print("el numero", num_uno, "NO cumple con la condicion. :( \n")

#disyunción
print("disyunción (or)")

palabra = input("para cumplir con la condición escribe 'si' o la palabra 'yes': ")
palabra = palabra.lower()

if palabra == "si" or palabra == "yes":
    print("la condicion se ha cumplido. :D \n")
else:
    print("la condición no se ha cumplido. :( \n")

#negación
print("negación(not)")

num_uno = int(input("introduce un numero diferente a 5: "))

if not num_uno == 5:
    print("el numero es diferente a 5 y si se cumple la condición. :D")
else:
    print("el numero es igual a 5 y NO se cumple la condición. :( \n")




