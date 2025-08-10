print('Actividad GA2-240201528-AA4\nAlgoritmo para sistematizar el cálculo de perímetros, áreas y volúmenes de figuras planas y sólidos regulares')

# Calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    return base * altura / 2
print('El área de un triángulo se calcula con su base * su altura / 2 ')

#Calcular perímetro de un triángulo
def calcular_perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3
print('El perímetro de un triangulo se calcula con la suma de sus 3 lados lado1 + lado2 + lado3')

#Calcular área de un cuadrado
def calcular_area_cuadrado(lado):
    return(2 * lado)

#Calcular perímetro de un cuadrado
def calcular_perimetro_cuadrado(lado):
    return 4 * lado
print('El perímetro de un cuadrado se calcula con la suma de sus 4 lados iguales o multiplicando uno de sus lados * 4')

#Calcular volumen de un cubo
def calcular_volumen_cubo(lado):
    return lado**3

#Calcular area de un rectangulo 
def calcular_area_rectangulo (base, altura):
    return base * altura
print('El área de un rectángulo se calcula con su base * su altura')

#Calcular perimetro rectangulo
def calcular_perimetro_rectangulo (base, altura):
    return 2 * base + 2 * altura
print('El perímetro de un rectangulo se calcula con 2 veces su base + 2 veces su altura')

#Calcular area de un circulo
def calcular_area_circulo(radio):
    return 3.1416 * radio**2

#Calcular perimetro de un circulo
def calcular_perimetro_circulo (radio):
    return 2 * 3.1416 * radio


#Elegir figura
def main():
    print("Calcular área y perímetro de figuras planas")
    print('1: Triángulo')
    print('2: Cuadrado')
    print('3: Rectángulo')
    print('4: Círculo')

    figura_var = int(input('Seleccione la figura con los números correspondientes 1/2/3/4: '))
    if figura_var == 1:
        def calculo():
            print('1: Área')
            print('2: Perímetro')
            calculo_var = int(input('Seleccione el cálculo que quiere realizar con su número correspondiente 1/2: '))
           
            if calculo_var == 1:
                base = float(input('Escriba la base del triángulo: '))
                altura = float(input('Escriba la altura del triángulo: '))
                area = calcular_area_triangulo(base, altura)
                print(f'el área del triangulo es: {area}')
            
            elif calculo_var == 2:
                lado1 = float(input('Escriba el lado 1 del triángulo: '))
                lado2 = float(input('Escriba el lado 2 del triángulo: '))
                lado3 = float(input('Escriba el lado 3 del triángulo: '))
                perimetro = calcular_perimetro_triangulo(lado1, lado2, lado3)
                print(f'El perímetro del triángulo es: {perimetro}')

            else:
                print("Número no disponible")

        calculo()
    
    if figura_var == 2:
        def calculo():
            print('1: Área')
            print('2: Perímetro')
            print('3: Volumen')
            calculo_var = int(input('Seleccione el cálculo que quiere realizar con su número correspondiente 1/2: '))

            if calculo_var == 1:
                lado = float(input('Escriba el lado del cuadrado: '))
                area = calcular_area_cuadrado(lado)
                print(f'El área del cuadrado es {area}')

            elif calculo_var == 2:
                lado = float(input('Escriba el lado del cuadrado: '))
                perimetro = calcular_perimetro_cuadrado(lado)
                print(f'El perimetro del cuadrado es: {perimetro}')

            elif calculo_var == 3:
                lado = float(input('Escriba el lado del cubo: '))
                volumen = calcular_volumen_cubo(lado)
                print(f'El volumen del cubo es: {volumen}')

            else:
                print('Número no disponible')
        
        calculo()

    if figura_var == 3:
        def calculo():
            print('1: Área')
            print('2: Perímetro')
            calculo_var = int(input('Seleccione el cálculo que quiere realizar con su número correspondiente 1/2: '))

            if calculo_var == 1:
                base = float(input('Escriba la base del rectángulo: '))
                altura = float(input('Escriba la altura del rectángulo: '))
                area = calcular_area_rectangulo(base, altura)
                print(f'El área del rectángulo es: {area}')

            elif calculo_var == 2:
                base = float(input('Escriba la base del rectángulo: '))
                altura = float(input('Escriba la altura del rectángulo: '))
                perimetro = calcular_perimetro_rectangulo(base, altura)
                print(f'El perímetro del rectángulo es: {perimetro}')

            else:
                print('Número no disponible')

        calculo()
    
    if figura_var == 4:
        def calculo():
            print('1: Área')
            print('2: Perímetro')
            calculo_var = int(input('Seleccione el cálculo que quiere realizar con su número correspondiente 1/2: '))

            if calculo_var == 1:
                radio = float(input('Escriba el radio del circulo: '))
                area = calcular_area_circulo(radio)
                print(f'el area del circulo es {area}')

            elif calculo_var == 2:
                radio = float(input('Escriba el radio del círculo: '))
                perimetro = calcular_perimetro_circulo(radio)
                print(f'el perimetro del círculo es {perimetro}')

            else:
                print('Número no disponible')
        
        calculo()

if __name__ == '__main__':
    main()