import random

def generate_random_list(length, start, end):
    result = []
    for i in range(length):
        result.append(random.randint(start, end))
    return result

def najwElement(list):
    if len(list) == 0:
        print('Error: Lista jest pusta')
        return

    result = list[0]
    for item in list:
        if result < item:
            result = item
    return result

myList = generate_random_list(5, -25, 25)

print(myList, "Najwiekszy element:", najwElement(myList))