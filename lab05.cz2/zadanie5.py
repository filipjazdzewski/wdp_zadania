lista = [8, -10, 5.5, 22, -18, 14]
maxElement = lista[0]
minElement = lista[0]

for element in lista:
    if element > maxElement:
        maxElement = element
    if element < minElement:
        minElement = element

print('Max:', maxElement)
print('Min:', minElement)