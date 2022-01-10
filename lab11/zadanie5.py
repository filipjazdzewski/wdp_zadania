import string

file = open('wiersz.txt', 'r')

smallLetters = 0
largeLetters = 0
digits = 0
whiteSpaces = 0

for line in file:
    for char in line:
        if char in string.ascii_lowercase:
            smallLetters += 1
        elif char in string.ascii_uppercase:
            largeLetters += 1
        elif char in string.digits:
            digits += 1
        elif char in string.whitespace:
            whiteSpaces += 1

print('Lowercase letters:', smallLetters)
print('Uppercase letters:', largeLetters)
print('Digits:', digits)
print('White Spaces:', whiteSpaces)
