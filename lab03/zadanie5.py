a = int(input('Podaj liczbe a:'))
b = int(input('Podaj liczbe b:'))

while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)