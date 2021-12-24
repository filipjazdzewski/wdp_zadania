napis = input('Wprowadz tekst:')
napis = napis.upper()
litery = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']


def eng_alphabet(napis):
    global litery
    for litera in litery:
        if litera not in napis:
            return False
    return True


print('Czy wszystkie litery w napisie?', eng_alphabet(napis))
