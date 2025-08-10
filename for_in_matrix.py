print()
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matrix)
print(f"{matrix[0]} \n{matrix[1]} \n{matrix[2]}")

#muestrame el número 1
#muestrame el número 4
#muestrame el número 8
#muestrame el número 3

print(matrix[0][0])
print(matrix[1][0])
print(matrix[2][1])
print(matrix[0][2])

matrix_1 = [[1, 2, 3],    #bucle for
            [4, 5, 6],
            [7, 8, 9]]

for row in matrix_1:
    print(row)

matrix_2 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

for row in matrix_2:
    for element in row:
        print(element)

matrix_3 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

for row in matrix_3:
    for element in row:
        print(element, end = " ")
    print()
