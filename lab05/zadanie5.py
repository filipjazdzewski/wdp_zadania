sixCharacters = input('Wprowadz 6 znakow z klawiatury:')

while len(sixCharacters) != 6:
    sixCharacters = input('Nie podales 6 znakow! Sprobuj ponownie:')

print(sixCharacters[4])     # 5 znak

print(sixCharacters[1:4])   # od 2 do 4

print(sixCharacters[-5:-2]) # od 2 do 4 (przez ujemne zakresy)
