def suma(a, b):
    result = a + b
    return result

dodawanie = suma(4, 5)
print(dodawanie)

print()#################################################################################

def sumaElementow(list):
    result = 0
    for item in list:
        result += item
    return result

listaTestowa = [4, 2, 11, 6]
wynikSpodziewany = 23

if wynikSpodziewany != sumaElementow(listaTestowa):
    print('Błąd!', wynikSpodziewany, sumaElementow(listaTestowa))
else:
    print(f'Dobrze! Suma elementow: {sumaElementow(listaTestowa)}'
          f' i wynik spodziewany: {wynikSpodziewany} są równe.')

print()#################################################################################

# Napisz funkcje która dla listy wartości wyznaczy element największy

def najwElement(list):
    if len(list) == 0:
        print('Error: Lista jest pusta')
        return
    else:
        result = list[0]
        for item in list:
            if result < item:
                result = item
        return result

listaWarosci = [-4, 10, -12, 15, 7, 0]
# listaWarosci = [] # w tym wypadku wyskoczy nam 'Error: Lista jest pusta'
print(najwElement(listaWarosci))

print()#################################################################################

# Napisz funkcje, która dla (zadanej) listy zwróci listę zawierającą co drugi element listy pierwszej

def coDrugi(list):
    result = []
    for i in range(len(list)):
        if i % 2 != 0:
            result.append(list[i])
    return result

listaTestowa2 = [-3, 5, 4, 10, 7, -8]
print(coDrugi(listaTestowa2))