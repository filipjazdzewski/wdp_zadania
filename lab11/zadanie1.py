def min_max(arr):
    if len(arr) == 0:
        print('Error: pusta lista!')
        return None
    my_min = arr[0]
    my_max = arr[0]

    for number in arr:
        if number > my_max:
            my_max = number
        if number < my_min:
            my_min = number

    return my_min, my_max


def format_list_to_int(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return arr


integers = open('liczby.txt', 'r')
integer_list = integers.read().split()

format_list_to_int(integer_list)

print(integer_list)
print(min_max(integer_list))
