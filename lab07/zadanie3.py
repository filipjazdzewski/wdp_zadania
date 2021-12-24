def min_max(num1, num2, num3):
    lista = [num1, num2, num3]
    lista.sort()
    return lista[0], lista[1]


krotka = (min_max(5, 18, 4))
print(krotka)
