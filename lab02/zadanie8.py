import math

a = int(input('Podaj 1 liczbe:'))
b = int(input('Podaj 2 liczbe:'))
c = int(input('Podaj 3 liczbe:'))
x1 = 0
x2 = 0
delta = b*b - 4*a*c

if delta < 0:
    print('Funkcja kwadratowa nie ma pierwiastkow.')
elif delta == 0:
    x1 = -b / 2*a
    print('Funkcja kwadratowa ma 1 pierwiastek:', x1)
else:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print('Funkcja kwadratowa ma 2 pierwiastki:', x1, x2)
