def bubble_sort(list_to_sort):
    n = len(list_to_sort)
    j = n - 2
    while j >= 0:
        i = 0
        while i <= j:
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
            i += 1
        j -= 1
    return list_to_sort


# GÓWNO NIE DZIALA
def binary_search(sorted_list, element, left, right):
    if left < right:
        middle = int((left+right)//2)
    else:
        if sorted_list[left] == element:
            return left
        else:
            return None
    if sorted_list[middle] < element:
        return binary_search(sorted_list, element, middle + 1, right)
    else:
        return binary_search(sorted_list, element, left, right)


my_list = [8, 3, 28, 12, 4, -5, 10, 9, -8, 21, 5]
my_list_sorted = bubble_sort(my_list)
result = binary_search(my_list_sorted, 10, 0, len(my_list_sorted)-1)
print(result)
