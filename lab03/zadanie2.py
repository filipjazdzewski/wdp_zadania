numerLiczby = 0
suma = 0
while True:
    numerLiczby += 1
    num = int(input(f"Podaj liczbe numer {numerLiczby}:"))
    if num != 0:
        suma += num
    if not num != 0:
        break
print(suma)