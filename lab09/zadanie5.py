def choice_sort(list_to_sort):
    n = len(list_to_sort) - 1
    j = 0
    while j < n:
        p = j
        i = j + 1
        while i <= n:
            if list_to_sort[i] < list_to_sort[p]:
                p = i
            i += 1
        list_to_sort[j], list_to_sort[p] = list_to_sort[p], list_to_sort[j]
        j += 1
    return list_to_sort


my_list = [8, 3, 12, 4, -5, 10, 9, 8]
result = choice_sort(my_list)
print(result)
