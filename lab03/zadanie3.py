liczbyDodatnie = 0
liczbyUjemne = 0
while True:
    num = int(input('Podaj liczbe:'))
    if num < 0:
        liczbyUjemne += 1
    if num > 0:
        liczbyDodatnie += 1
    if not num != 0:
        break

print(f'Liczb ujemnych jest {liczbyUjemne}, a liczb dodatnich {liczbyDodatnie}')