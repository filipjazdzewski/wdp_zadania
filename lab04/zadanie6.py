n = int(input('Podaj liczbe n:'))
for i in range(1, n+1):
    print((n-i)*" " + i*"*" + (i-1)*"*")

print((n-2)*" " + "|_|")