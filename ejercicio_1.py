print("Sistema de control vacacional de empresas. \n")

nombre_empleado = input("¿Cuál es su nombre completo?: ")
clave_de_departamento = int(input("¿Cuál es su clave?, solo existen claves del 1 al 3: "))
años_de_trabajo = float(input("¿Cuántos años lleva trabajando en la empresa?: \n"))

if clave_de_departamento == 1:

    if años_de_trabajo == 1 and años_de_trabajo < 2:
        print("el empleado", nombre_empleado, " merece 6 dias de vacaciones.")
    elif años_de_trabajo >= 2 and años_de_trabajo <= 6:
        print("el empleado", nombre_empleado, " merece 14 dias de vacaciones.")
    elif años_de_trabajo >=7:
        print("el empleado", nombre_empleado, "merece 20 dias de vacaciones.")
    else:
        print("aun no tiene derecho a vacaciones")
    
elif clave_de_departamento == 2:
    
    if años_de_trabajo == 1 and años_de_trabajo < 2:
        print("el empleado", nombre_empleado, " merece 7 dias de vacaciones.")
    elif años_de_trabajo >= 2 and años_de_trabajo <= 6:
        print("el empleado", nombre_empleado, " merece 15 dias de vacaciones.")
    elif años_de_trabajo >=7:
        print("el empleado", nombre_empleado, "merece 22 dias de vacaciones.")
    else:
        print("aun no tiene derecho a vacaciones")

elif clave_de_departamento == 3:
    if años_de_trabajo == 1 and años_de_trabajo < 2:
        print("el empleado", nombre_empleado, "merece 10 dias de vacaciones.")
    elif años_de_trabajo >= 2 and años_de_trabajo <=6:
        print("el empleado", nombre_empleado, "merece 20 dias de vacaciones")
    elif años_de_trabajo >= 7:
        print("el empleado", nombre_empleado, "merece 30 dias de vacaciones")

else:
    clave_no_valida = print("no se puede determinar el valor si su clave no es del 1 al 3")
