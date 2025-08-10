import random

print("Bienvenido al juego de piedra, papel o tijeras")

# opciones de juego
opciones = ["piedra", "papel", "tijeras"]

# función para obtener la elección del usuario
def obtener_eleccion_usuario():
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while eleccion_usuario not in opciones:
        eleccion_usuario = input("Por favor, elige piedra, papel o tijeras: ")
    return eleccion_usuario

# función para obtener la elección de la computadora
def obtener_eleccion_computadora():
    eleccion_computadora = random.randint(1, 3)
    if eleccion_computadora == 1:
        return "piedra"
    elif eleccion_computadora == 2:
        return "papel"
    else:
        return "tijeras"

# función para determinar el ganador
def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijeras") or (usuario == "papel" and computadora == "piedra") or (usuario == "tijeras" and computadora == "papel"):
        return "¡Ganaste!"
    else:
        return "Perdiste :("

# ciclo principal del juego
while True:
    eleccion_usuario = obtener_eleccion_usuario()
    eleccion_computadora = obtener_eleccion_computadora()
    print(f"Tú elegiste {eleccion_usuario} y la computadora eligió {eleccion_computadora}")
    resultado = determinar_ganador(eleccion_usuario, eleccion_computadora)
    print(resultado)
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
    if jugar_de_nuevo.lower() != "s":
        break

print("¡Gracias por jugar!")
