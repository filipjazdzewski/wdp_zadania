n = int(input('Podaj calkowita liczbe dodatnia:'))

suma = 0

for m in range(1, n+1, 1):
    if (suma + m) > n:
        m -= 1
        break
    else:
        suma += m

print(m)



