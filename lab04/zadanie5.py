n = int(input("Podaj liczbe n:"))
for i in range(1, n + 1):
    print(i*"*")

print("")

for i in range(0, n):
    print((n-i)*"*")