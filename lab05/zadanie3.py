word = input('Podaj slowo:')
newWord = ''
for letter in word:
    if letter == 'ą':
        newWord += 'a'
    elif letter == 'ć':
        newWord += 'c'
    elif letter == 'ę':
        newWord += 'e'
    elif letter == 'ł':
        newWord += 'l'
    elif letter == 'ń':
        newWord += 'n'
    elif letter == 'ó':
        newWord += 'o'
    elif letter == 'ś':
        newWord += 's'
    elif letter == 'ź' or letter == 'ż':
        newWord += 'z'
    else:
        newWord += letter

print(newWord)


