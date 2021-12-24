def is_element_the_biggest(el, my_list):
    if len(my_list) == 0:
        return True
    if my_list[0] <= el:
        return is_element_the_biggest(el, my_list[1:])
    else:
        return False


element = 17
list_of_numbers = [-5, 4, 12, -11, 13, 17, 9, 15]
if element in list_of_numbers:
    result = is_element_the_biggest(element, list_of_numbers)
else:
    result = None
print(result)
