# dziala dla tablic z liczba wierszy parzysta i nieparzysta

matrix = [
    [1.0, 2.0, 3.0, 5.0],
    [4.0, 5.0, 6.0, 4.0],
    [7.0, 8.0, 9.0, 2.0],
    [5.0, 2.0, 1.0, 4.0],
]

for wiersz in matrix:
    for element in wiersz:
        print(element, end=" ")
    print()

suma_przekatnych = 0
# poniewaz liczba wierszy = liczba elementow w wierszach nie musimy dawac matrix[i] w 2 petli for
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j or (len(matrix) - i - 1) == j:
            suma_przekatnych += matrix[i][j]

print('Suma przekatnych wynosi:', suma_przekatnych)
