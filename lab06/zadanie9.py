chessboard = [
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', 'H', '_', '_', '_', 'H'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['H', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', 'P', '_', '_', '_'],
]

isEndangered = False
numOfRows = len(chessboard)


# narysowanie szachownicy
print('\n    CHESS BOARD')
for row in chessboard:
    print(numOfRows, end=' ')
    for element in row:
        print(element, end=' ')
    print()
    numOfRows -= 1
print('  A B C D E F G H')

# znalezienie pozycji Piona
for i in range(len(chessboard)):
    for j in range(len(chessboard)):
        if chessboard[i][j] == 'P':
            pawnRow = i
            pawnColumn = j

# sprawdzenie czy w Rzedzie Piona znajduje sie Hetman
for i in range(len(chessboard)):
    if chessboard[pawnRow][i] == 'H':
        isEndangered = True

# sprawdzenie czy w Kolumnie Piona znajduje sie Hetman
for i in range(len(chessboard)):
    if chessboard[i][pawnColumn] == 'H':
        isEndangered = True

# sprawdzanie ukosnych
rightDown = pawnColumn
leftDown = pawnColumn
rightUp = pawnColumn
leftUp = pawnColumn
# dolne ukosne od Piona
for i in range(pawnRow + 1, len(chessboard)):
    if leftDown > 0:
        leftDown -= 1
        if chessboard[i][leftDown] == 'H':
            isEndangered = True
    if rightDown < len(chessboard) - 1:
        rightDown += 1
        if chessboard[i][rightDown] == 'H':
            isEndangered = True

print('---------------------')

# gorne ukosne od Piona
for i in range(pawnRow - 1, -1, -1):
    if leftUp > 0:
        leftUp -= 1
        if chessboard[i][leftUp] == 'H':
            isEndangered = True
    if rightUp < len(chessboard) - 1:
        rightUp += 1
        if chessboard[i][rightUp] == 'H':
            isEndangered = True

if isEndangered:
    print('Pion jest zagrozony.')
else:
    print('Pion nie jest zagrozony.')
