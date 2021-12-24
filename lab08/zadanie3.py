def fibonacci_number(num):
    if num < 0:
        return None
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci_number(num-2) + fibonacci_number(num-1)


result = int(input('Ktora liczba ciagu fibonacciego:'))
print(fibonacci_number(result))

# fibonacci_number(4) = fibonacci_number(2) + fibonacci_number(3) =
# = fibonacci_number(0) + fibonacci_number(1) + fibonacci_number(1) + fibonacci_number(2) =
# = 0 + 1 + 1 + fibonacci_number(0) + fibonacci_number(1) = 0 + 1 + 1 + 0 + 1 = 3
