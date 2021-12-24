k = int(input('Podaj k:'))

matrix = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0]
]

for wiersz in matrix:
    for element in wiersz:
        print(element * k, end=" ")
    print()
