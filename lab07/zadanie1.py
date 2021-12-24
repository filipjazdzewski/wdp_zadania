def iloczyn_2_liczb(num1, num2):
    for i in range(1, num2 + 1):
        wynik = i * num1
        print(f"{i} * {num1} = {wynik}")

a = int(input('Podaj a:'))
n = int(input('Podaj n:'))
iloczyn_2_liczb(a, n)
