matrix = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
]

for w in matrix:
    for x in w[::-1]:
        print(x, end=" ")
    print()
