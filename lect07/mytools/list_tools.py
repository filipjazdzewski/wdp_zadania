import random


def create_random_list(size, start=-100, end=100):
    result = []
    for i in range(size):
        result.append(random.randint(start, end))
    return result


def copy_list(list):
    result = []
    for item in list:
        result.append(item)
    return result
