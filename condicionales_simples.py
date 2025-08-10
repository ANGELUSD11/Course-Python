print("sistema para calcular el promedio de un alumno")
nombre = input("introduce tu nombre: ")

matematicas = float(input(nombre + " ¿Cuál es tu calificación en matematicas?: "))
quimica = float(input(nombre + " ¿Cuál es tu calificación en quimica?: "))
biologia = float(input(nombre + " ¿Cuál es tu calificación en biologia?: "))

promedio = (matematicas + quimica + biologia) / 3
if promedio >= 3.5:
    print('felicidades '+ nombre + ' "aprobaste" con un promedio de: ', promedio)

if promedio < 3.5:
    print('lo sentimos "no aprobaste"')

print("fin")




    



