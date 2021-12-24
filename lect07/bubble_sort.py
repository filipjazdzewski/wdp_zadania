import mytools.list_tools


def bubble_sort(list):
    sorted_list = mytools.list_tools.copy_list(list)

    for j in range(len(sorted_list)):
        for i in range(len(sorted_list) - 1 - j):
            if sorted_list[i + 1] < sorted_list[i]:
                tmp = sorted_list[i]
                sorted_list[i] = sorted_list[i + 1]
                sorted_list[i + 1] = tmp

    return sorted_list


some_list = mytools.list_tools.create_random_list(10, -50, 50)
some_list_sorted = bubble_sort(some_list)

print(some_list)
print(some_list_sorted)
some_list.sort()    # wbudowane sortowanie
print(some_list)
