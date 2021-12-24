word = input('Podaj slowo:')
pattern = input('Wprowadz wzorzec:')
patternOccurrence = False

# 1 method
if pattern in word:
    print('Wzorzec pojawia sie w slowie.')
else:
    print('Wzorzec nie pojawia sie w slowie.')

# 2 method
if len(pattern) <= len(word):
    for i in range(len(word)):
        if (word[i:i+len(pattern)]) == pattern:
            patternOccurrence = True
if patternOccurrence:
    print('Wzorzec pojawia sie w slowie.')
else:
    print('Wzorzec nie pojawia sie w slowie.')
