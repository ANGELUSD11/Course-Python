#conceptos de operadores aritméticos, de comparación y lógicos

#variables

#personaje
edad = 20
print("la edad actual de nuestro personaje es: ", edad)

#constantes
#pyhton no tiene constantes, pero se usa la convención mayuscula, no bloquea la reasignación

NOMBRE = "Juan"


edad += 5
print("Pasaron 5 años...")
print("Nuestro personaje ha crecido, su edad actual es: ", edad)

vida = 100
print(f"la vida inicial de nuestro personaje {NOMBRE} es: {vida}")
print("Un enemigo ha atacado!")

nivel_escudo = 20

#enemigo
ataque = 20

def calcular_daño(vida, ataque):
    vida -= ataque
    return vida

#ahora la variable vida tiene un nuevo valor
vida = calcular_daño(vida, ataque)
print(f"Tu vida actual es {vida}")

#en este caso la variable cambió su valor
print("El ataque del enemigo ha aumentado!")
ataque = 50

vida = calcular_daño(vida, ataque)
print(f"Tu vida actual es {vida}")

#operadores relacionales
if vida <= 50:
    print("Te han quitado media vida")

#operadores lógicos
if vida <= 50 and nivel_escudo < 30 or vida <= 20 and nivel_escudo < 10:
    print("Tienes poca vida y tu escudo es débil, ten cuidado")
