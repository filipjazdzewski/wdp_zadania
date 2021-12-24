napis = 'kontrabanda'

print(napis.count('a'))

print(napis.replace('a', 'x'))

print(napis[1:5])

print(napis[0:6])

l = [3*c-4 for c in range(5)]
print(l)
for i in range(3):
    if i not in l:
        l.append(i)
    else:
        l.append(-1*i)
print(l)