def czy_zbudujesz_trojkat(a, b, c):
    if czy_dodatnie(a, b, c):
        lista = [a, b, c]
        lista.sort()
        if lista[0] + lista[1] > lista[2]:
            return True
    return False


def czy_dodatnie(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return True
    print('Bok musi miec dlugosc dodatnia.')
    return False


answer = czy_zbudujesz_trojkat(4, 3, 8)
if answer:
    print('Mozna zbudwac trojkat.')
else:
    print('Nie mozna zbudowac trojkata.')
