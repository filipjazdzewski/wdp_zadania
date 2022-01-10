from random import randint

lottery = open('lotto.txt', 'w')
numbers = []
for i in range(6):
    while True:
        number = str(randint(1, 49))
        if number not in numbers:
            break
    numbers.append(number)

    lottery.write(numbers[i] + ' ')
