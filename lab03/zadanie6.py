bin = input('Podaj liczbe w systemie binarnym:')
liczbaDzies = 0

for i in range(1, len(bin)+1):
    liczbaDzies+=int(bin[len(bin)-i])*(2**(i-1))
print(liczbaDzies)
