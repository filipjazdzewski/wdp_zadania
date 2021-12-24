def insert_sort(list_to_sort):
    n = len(list_to_sort) - 1
    j = n - 1
    while j >= 0:
        p = list_to_sort[j]
        i = j + 1
        while i <= n and p < list_to_sort[i]:
            list_to_sort[i - 1] = list_to_sort[i]
            i += 1
        list_to_sort[i - 1] = p
        j -= 1
    return list_to_sort


my_list = [8, 3, 12, 4, -5, 10, 9, 8]
result = insert_sort(my_list)
print(result)

# jedyna zmiana byla w linii 7 (znak wiekszosci zmnieniony na mniejszosci)
