import random

integer_list = [random.randint(-50, 50) for i in range(10)]

even = open('parzyste.txt', 'w')
odd = open('nieparzyste.txt', 'w')

for number in integer_list:
    if number % 2 == 0:
        number = str(number)
        even.write(number + ' ')
    else:
        number = str(number)
        odd.write(number + ' ')
