matrix1 = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
]
matrix2 = [
    [8.0, 7.0, 5.0],
    [3.0, 4.0, 1.0],
]

for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        print(matrix1[i][j] + matrix2[i][j], end=" ")
    print()
