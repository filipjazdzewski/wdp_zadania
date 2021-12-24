firstWord = input('Podaj 1 slowo:')
secondWord = input('Podaj 2 slowo:')

if firstWord < secondWord:
    print('Slowo 1 jest predzej w porzadku leksykograficznym.')
elif firstWord == secondWord:
    print('Slowo 1 i 2 sa takie same.')
else:
    print('Slowo 2 jest predzej w porzadku leksykograficznym.')

if len(firstWord) > len(secondWord):
    print('Slowo 1 jest dluzsze.')
elif len(firstWord) == len(secondWord):
    print('Slowo 1 i 2 maja taka sama dlugosc.')
else:
    print('Slowo 2 jest dluzsze.')

