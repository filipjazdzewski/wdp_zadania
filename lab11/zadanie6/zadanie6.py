words = open('znaki.txt', 'r')
palindromes = open('palindrom.txt', 'w')

arr = words.read().split()
count = 0

for word in arr:
    if word == word[::-1]:
        palindromes.write(f'{word} ')
        count += 1
print(f'Ilosc palindromow: {count}')
