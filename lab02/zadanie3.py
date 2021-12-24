a = int(input('Podaj 1 liczbe:'))
b = int(input('Podaj 2 liczbe:'))
c = int(input('Podaj 3 liczbe:'))

if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if b >= c:
        print(b)
    else:
        print(c)
