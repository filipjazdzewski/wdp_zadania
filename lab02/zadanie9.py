n = int(input('Podaj liczbe n:'))

if n > -10 and n < 10:
    print(f'Liczba {n} jest 1-cyfrowa.')
elif n > -100 and n < 100:
    print(f'Liczba {n} jest 2-cyfrowa.')
elif n > -1000 and n < 1000:
    print(f'Liczba {n} jest 3-cyfrowa.')
else:
    print(f'Liczba {n} ma wiecej niz 3 cyfry, wiec jest z poza zakresu.')
