matrix = [
    [1.0, 2.0, 3.0],
    [16.0, 8.0],
    [-2.0, 4.0, 5.0],
    [5.0, -22.0]
]
maxLine = 0
sumLine = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        sumLine += matrix[i][j]
    if sumLine > maxLine:
        maxLine = sumLine
        maxLineIndex = i
    sumLine = 0

print('Numer indeksu wiersza z najwieksza suma elementow:', maxLineIndex)
print('Suma elementow tego wiersza:', maxLine)




