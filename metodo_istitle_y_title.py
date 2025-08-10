print("programa de prueba\n")
nombres = input("introduzca sus nombres: ")
apellidos = input("introduzca sus apellidos: ")
nombre_completo = f"{nombres} {apellidos}"

print()
print(f"el formato del metodo title se ha aplicado?: {nombre_completo.istitle()}")
print(f"aplicando el metodo title(): {nombre_completo.title()}")
print(f"volvemos a imprimir el nombre: {nombre_completo}")
print()
nombre_completo = nombre_completo.title()
print(f"¿El formato del metodo title se ha aplicado?: {nombre_completo.istitle()}")
print(f"Se ha aplicado el metodo title de manera permanente: {nombre_completo}")
