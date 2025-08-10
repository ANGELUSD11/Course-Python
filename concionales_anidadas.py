print("conversor \n")

print("menu de opciones \n")
print("presiona 1 para convertir un numero del 1 al 5 a palabra")
print("presiona 2 para convertir de palabra del uno al cinco a numero \n")

opcion = int(input("¿cual es tu opcion deseada?: "))

if opcion == 1:
    print("\n conversor de numero a palabra \n.")

    opcion_uno = int(input("¿cual es el numero que deseas convertir a palabra?: "))

    if opcion_uno == 1:
        print("el numero es 'UNO'")
    elif opcion_uno ==2:
        print("el numero es 'DOS")
    elif opcion_uno ==3:
        print("el numero es 'TRES'")
    elif opcion_uno ==4:
        print("el numero es 'CUATRO'")
    elif opcion_uno ==5:
        print("el numero es 'CINCO'")
    else:
        print("numero no registrado")
    
elif opcion == 2:
    print("\n conversor de palabra a numero \n.")

    opcion_dos = input("¿cual es la palabra que deseas convertir a numero?: ")
    opcion_dos = opcion_dos.lower()
    
    if opcion_dos == "uno":
        print("la palabra es '1'")
    elif opcion_dos == "dos":
        print("la palabra es '2'")
    elif opcion_dos == "tres":
        print("la palabra es '3'")
    elif opcion_dos == "cuatro":
        print("la palabra es '4'")
    elif opcion_dos == "cinco":
        print("la palabra es '5'")
    else:
        print("palabra no registrada")
    
else:
    print("opcion no disponible")

print("fin.")
    
    
    
