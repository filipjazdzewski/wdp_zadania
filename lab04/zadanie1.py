n = int(input('Podaj liczbe n:'))
suma = 0
for i in range(n):
    liczba = float(input('Podaj kolejna liczbe:'))
    suma += liczba
print('Srednia arytmetyczna wynosi:', suma / n)