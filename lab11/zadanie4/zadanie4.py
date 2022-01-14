data_base = open('baza.txt', 'r')

searched_name = 'Karol'
searched_surname = 'Jagielski'

people = {}

for line in data_base:
    arr = line.split()
    people[f'imie{arr[0]}'] = arr[1]
    people[f'nazwisko{arr[0]}'] = arr[2]
    people[f'miejscowosc{arr[0]}'] = arr[3]
    if arr[1] == searched_name and arr[2] == searched_surname:
        print(f'{searched_name} {searched_surname} jest w bazie.')

print(people)