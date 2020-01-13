"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from array import array

def find_sum(arr):
    """
     function returns sum between min and max array items
    :param arr: array of numbers
    :return: float - result
    """
    min_val = max_val = arr[0]
    min_index = max_index = 0
    result = 0.0
    if len(arr) < 2:
        print(f"Array {arr} is too short")
    for i, item in enumerate(arr):
        if item < min_val:
            min_val = item
            min_index = i
        if item > max_val:
            max_val = item
            max_index = i
    if max_index < min_index:
        max_index, min_index = min_index, max_index
    print(f"MIN_INDEX={min_index}, MAX_INDEX={max_index}")
    for j in range(min_index + 1, max_index):
        result += arr[j]
        print(j, " ", result)
    return result

TEST_ARRAY1 = array('i', [0, -3, -8, -10, 19, 1, 200])
TEST_ARRAY2 = array('f', [100.0, -12.2, 1.1, -2.2, -1.0, -0.003, -34.0, 12.0])
print(str(find_sum(TEST_ARRAY1)))
print(str(find_sum(TEST_ARRAY2)))
