import random

def generate_random_list(length, start, end):
    generated_list = []
    for i in range(length):
        generated_list.append(random.randint(start, end))
    return generated_list

def min_max(list):
    if len(list) == 0:
        print('Error: pusta lista!')
        return
    my_min = list[0]
    my_max = list[0]

    for number in list:
        if number > my_max:
            my_max = number
        if number < my_min:
            my_min = number

    return my_max, my_min

my_list = generate_random_list(10, -50, 50)
print(my_list, min_max(my_list))