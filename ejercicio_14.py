#suma de matrizes especificada por usuario

number_of_matrix = int(input("¿Cuántas matrizes vamos a sumar?: "))

if number_of_matrix > 1:
    rows_of_matrix = int(input("¿cuantas filas tendran las matrices?: "))
    columns_of_matrix = int(input("cuantas columnas tendran las matrices?: "))

    matrix_list = []

    #llenado de matrices
    for number in range(number_of_matrix):
        matrixes = []
        for rows in range(rows_of_matrix):
            new_row_2 = []
            for columns in range(columns_of_matrix):
                new_row_2.append(

                int(input(f"introduce un elemento para la matriz {number + 1} fila {rows}, columna {columns}")))
            matrixes.append(new_row_2)
        matrix_list.append(matrixes)

    #suma de las matrices
    all_matrixes = []
    for row in range(rows_of_matrix):
        new_row_3 = []
        for column in range(columns_of_matrix):
            sum_matrix = 0
            for matrix_position in range(len(matrix_list)):
                sum_matrix += matrix_list[matrix_position][rows][columns]
            new_row_3.append(sum_matrix)
        matrixes.append(new_row_3) 
    matrix_list.append(matrixes)

    #imprimir
    for matrix_row in range(rows):
        for matrix_list_position in range(len(matrix_list)):
            if matrix_row != 1:
                print(f"{matrix_list[matrix_list_position][matrix_row]}", end="    ")
            else:
                if matrix_list_position < len(matrix_list) - 2:
                    print(f"{matrix_list[matrix_list_position][matrix_row]}", end=" + ")
                elif matrix_list_position < len(matrix_list) -1:
                    print(f"{matrix_list[matrix_list_position][matrix_row]}", end=" = ")
                else:
                    print(f"{matrix_list[matrix_list_position][matrix_row]}", end="   ")
        
        print()

else:
    print("se necesitan 2 o más matrices para realizar la suma")
