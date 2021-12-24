lista1 = [5, 7.7, -12, 4, 11]
lista2 = [8, -3, 6.4, 15, 2]
iloczynSkalarny = 0

for i in range(len(lista1)):
    iloczynSkalarny += lista1[i] * lista2[i]
    print(lista1[i] * lista2[i])

print('Iloczyn skalarny wynosi =', iloczynSkalarny)