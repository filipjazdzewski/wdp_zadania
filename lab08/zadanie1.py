def get_factorial(num):
    if num < 0:
        return None
    if num < 2:
        return 1
    return num * get_factorial(num-1)


result = int(input('Podaj liczbe naturalna:'))
print(get_factorial(result))

# get_factorial(5) = 5 * get_factorial(4) = 5 * 4 * get_factorial(3) =
# = 5 * 4 * 3 * get_factorial(2) = 5 * 4 * 3 * 2 * get_factorial(1) =
# = 5 * 4 * 3 * 2 * 1 = 120
