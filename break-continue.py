#break
print("while con la sentencia break \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        break

    print("valor actual de la variable", contador)

print("fin del programa, la sentencia break se ha ejecutado.")

#continue
print("while con la sentencia continue \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        continue

    print("valor actual de la variable", contador)

if contador == 10:
    print("el programa ha finalizado")
