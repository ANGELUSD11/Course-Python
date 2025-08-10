print("sistema para calcular el promedio de un alumno")
nombre = input("introduce tu nombre: ")

matematicas = float(input(nombre + " ¿Cuál fue tu calificación en matematicas?: "))
quimica = float(input(nombre + " ¿Cuál fue tu calificación en quimica?: "))
biologia = float(input(nombre + " ¿Cuál fue tu calificación en biologia?: "))

promedio = (matematicas + quimica + biologia) / 3

if promedio >=3.5:
    print("felicidades " + nombre + " has 'aprobado' con un promedio de: ",round(promedio,1))
else:
    print("lo sentimos " + nombre + " has 'reprobado' con un promedio de: ",round(promedio,1))

print("fin.")
    
