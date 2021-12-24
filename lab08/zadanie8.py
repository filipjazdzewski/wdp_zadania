def sum_of_digits(num):
    if len(num) == 0:
        return 0
    return sum_of_digits(num[1:]) + int(num[0])


result = input('Podaj liczbe calkowita nieujemna:')
print(sum_of_digits(result))
