#matriz especificada por el usuario

rows = int(input("¿Cuántas filas tendrá la matriz?: "))
columns = int(input("¿Cuántas columnas tendrá la matriz?: "))

matrix = []

for row_position in range(rows):
    row = []
    for element in range(columns):
        row.append(int(input(f"introduce un elemento a la fila {row_position}:")))
    matrix.append(row)
    
for row in matrix:
    print(row)

#suma de matrizes

matrix_a = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_b = [[1, 2, 3],
            [4, 1, 2],
            [1, 1, 0]]

matrix_c = []

for row in range(len(matrix_a)):
    new_row = []
    for column in range(len(matrix_a[0])):
        new_row.append(matrix_a[row][column] + matrix_b[row][column])
    matrix_c.append(new_row)
    
for row in range(matrix_a):
    print(f"{matrix_a[row]} + {matrix_b[row]} = {matrix_c[row]}")







