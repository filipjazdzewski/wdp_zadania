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


def binary_search(sorted_list, element):    # binary_search potrzebuje posortowanej listy zeby dzialal
    sorted_list = bubble_sort(sorted_list)
    print(sorted_list)
    n = len(sorted_list)
    left = 0
    right = n - 1
    while left < right:
        middle = (left + right) // 2
        if sorted_list[middle] < element:
            left = middle + 1
        else:
            right = middle
    if sorted_list[left] == element:
        return left
    else:
        return None


my_list = [8, 3, 28, 12, 4, -5, 10, 9, -8, 21, 5]
result = binary_search(my_list, 10)
print(result)
