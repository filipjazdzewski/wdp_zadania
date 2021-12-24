word = input('Podaj slowo:')
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
numberOfVowels = 0

for letter in word:
    if letter in vowels:
        numberOfVowels += 1

print(numberOfVowels)