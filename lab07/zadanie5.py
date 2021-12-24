import random


def random_numbers(length, start, end):
    list = []
    for i in range(length):
        list.append(random.randint(start, end))
    return list


print(random_numbers(10, -100, 100))
