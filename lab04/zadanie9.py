password = input('Podaj haslo:')
n = int(input('Podaj ilosc powtorzen:'))

for i in range(1, n+1):
    checkPassword = input((f'Powtorz haslo {i}:'))
    while checkPassword != password:
        checkPassword = input((f'Powtorz haslo {i}:'))

print(f'Dziekuje podales prawidlowe haslo {n} razy')
