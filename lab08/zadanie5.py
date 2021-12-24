def sum_of_list_elements(my_list):
    if len(my_list) == 0:
        return 0
    return sum_of_list_elements(my_list[1:]) + my_list[0]


result = sum_of_list_elements([4, -5, 10, 31, -8, 13])
print(result)
