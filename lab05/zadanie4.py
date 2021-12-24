sentance = input('Wprowadz zdanie:')
count = 0

if sentance != '':
    count = 1

for letter in sentance:
    if letter == ' ' and lastLetter != ' ':
        count += 1
    lastLetter = letter

print(count)