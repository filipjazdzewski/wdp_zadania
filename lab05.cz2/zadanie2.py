lista = [1, 'Okej', False, 2, 3.0, 4, 5]
print(lista)
# pierwszy sposób
print(lista[::-1])
# drugi sposób
dlugoscListy = len(lista) - 1
nowaLista = []
while dlugoscListy >= 0:
    nowaLista.append(lista[dlugoscListy])
    dlugoscListy -= 1
print(nowaLista)
