word1 = input('Podaj 1 slowo:')
word2 = input('Podaj 2 slowo:')

newWord = ''
i = 0
if len(word1) >= len(word2):
    for letter in word1:
        newWord += letter
        if i < len(word2):
            newWord += word2[i]
            i += 1
else:
    for letter in word2:
        if i < len(word1):
            newWord += word1[i]
            i += 1
        newWord += letter

print(newWord)
