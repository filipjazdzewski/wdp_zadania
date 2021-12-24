# Słownik / { klucz : wartość, }

osoba1 = {
    'imie': 'Jan',
    'nazwisko': 'Przysłowiowy-Kowalski',
    'rokUrodzenia': 1978
}
osoba2 = {
    'imie': 'Janina',
    'nazwisko': 'Przysłowiowa-Kowalska',
    'rokUrodzenia': 1979
}

print(osoba2['nazwisko'], osoba1['rokUrodzenia'])

panstwo1 = {
    'ustroj': 'demokracja',
    'nazwa': 'USA',
    'stolica': 'Waszyngton',
    'jezyk': 'en_US',
    'liczba_mieszkancow': 330000000,
    'czy_w_nato': True
}
panstwo2 = {
    'ustroj': 'demokracja',
    'nazwa': 'Niemcy',
    'stolica': 'Berlin',
    'jezyk': 'de',
    'liczba_mieszkancow': 83000000,
    'czy_w_nato': True
}

baza_danych = [panstwo1, panstwo2]

print(baza_danych[0]['liczba_mieszkancow'])

def policz_mieszkancow(db):
    result = 0
    for panstwo in db:
        result += panstwo['liczba_mieszkancow']
    return result

print(policz_mieszkancow(baza_danych))