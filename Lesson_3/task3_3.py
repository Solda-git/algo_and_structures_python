"""
3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
"""

def change_minmax(list_param):
    """
    function changes max and min items in the list
    :param list: input list
    :return: result list
    """
    min_item = list_param[0]
    max_item = list_param[0]
    min_index = 0
    max_index = 0
    for (i, item) in enumerate(list_param):
        if item < min_item:
            min_item = item
            min_index = i
        if item > max_item:
            max_item = item
            max_index = i
    print(f"min item = {list_param[min_index]}, min index = {min_index}")
    print(f"max item = {list_param[max_index]}, max index = {max_index}")
    list_param[min_index], list_param[max_index] = list_param[max_index], list_param[min_index]
    return list_param

print(change_minmax([8, 3, 15, 6, 4, 2]))
print(change_minmax([8, 3, 15, 6, 4, 2, -23, -70, 12, 0, 5, 122, 1]))
print(change_minmax([-1, -3, -6, 0, 7]))
