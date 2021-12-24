# Macierz 2 wiersze, 3 kolumny
macierz2x3 = [[1, 2, 3],
              [4, 5, 6]]

# Macierz trójwymiarowa
macierz2x3x4 = [
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]],
    [[13, 14, 15, 16],
     [17, 18, 19, 20],
     [21, 22, 23, 24]]
]

for macierz2 in macierz2x3x4:
    for wiersz in macierz2:
        for element in wiersz:
            print(element)




