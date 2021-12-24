def bubble_sort(list_to_sort):
    n = len(list_to_sort)
    j = n - 2
    while j >= 0:
        i = 0
        while i <= j:
            if list_to_sort[i] < list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
            i += 1
        j -= 1
    return list_to_sort


my_list = [8, 3, 12, 4, -5, 10, 9, 8]
result = bubble_sort(my_list)
print(result)

# jedyna zmiana byla w linii 7 (znak wiekszosci zmnieniony na mniejszosci)
