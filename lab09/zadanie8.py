def bubble_sort(list_to_sort):  # ładnejszy bubble sort z pętlą for
    for j in range(len(list_to_sort) - 1):
        for i in range(len(list_to_sort) - j - 1):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
    return list_to_sort


def binary_search(sorted_list, element, left, right):  # lista musi być posortowana, podczas wywolywania funkcji za parametr left dac liczbe 0 a za parametr right liczbe len(list) - 1
    if left < right:
        middle = (left + right) // 2
    else:
        if sorted_list[left] == element:
            return left
        return None
    if sorted_list[middle] < element:
        return binary_search(sorted_list, element, middle + 1, right)
    else:
        return binary_search(sorted_list, element, left, middle)


my_list = [8, 3, 28, 12, 4, -5, 10, 9, -8, 21, 5]
my_list_sorted = bubble_sort(my_list)
my_element = 12
result = binary_search(my_list_sorted, my_element, 0, len(my_list_sorted)-1)
print(my_list_sorted)
print(result)
