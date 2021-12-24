word = input('Podaj slowo:')
newWord = ''

for i in range(len(word)-1, -1, -1):
    newWord += word[i]

print('Odwrocone slowo:', newWord)

if word == newWord:
    print('Slowo', word, 'jest palindromem.')
else:
    print('Slowo', word, 'nie jest palindromem.')
