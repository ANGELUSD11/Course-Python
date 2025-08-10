string = "Diana se peina sola"
resultado = 0
star_with = "Ejemplos con starswith: "
end_with = "Ejemplos con endswith: "

print(f"\n{star_with.rjust{50, '"'}}")

resultado = sring.starswith("D")
print(f"\n{string} comienza con la subcadena D?: {resultado} ")


resultado = sring.starswith("d")
print(f"\n{string} comienza con la subcadena d?: {resultado} ")


resultado = sring.starswith("se", 6)
print(f"\n{string} comienza con la subcadena se?, desde la posición 6: {resultado} ")


resultado = sring.starswith("se", 6, 7)
print(f"\n{string} comienza con la subcadena se?, desde la posición 6 hasta la posición 7: {resultado} ")


resultado = sring.starswith("se", 100, 100)
print(f"\n{string} comienza con la subcadena se?, desde la posición 100 hasta la posición 100: {resultado} ")


resultado = sring.starswith("se", -4, -1)
print(f"\n{string} comienza con la subcadena se?, desde la posición -4 hasta la posición -1: {resultado} ")


print(f"\n{end_with.rjust{50, '"'}}")

resultado = sring.endswith("A")
print(f"\n{string} termina con la subcadena A?: {resultado} ")


resultado = sring.endswith("a")
print(f"\n{string} termina con la subcadena a?: {resultado} ")


resultado = sring.endswith("sola")
print(f"\n{string} termina con la subcadena sola?: {resultado} ")







