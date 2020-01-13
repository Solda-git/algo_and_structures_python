"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
from array import array

def get_min(arr):
    """
        Function returns two minimal items of tye array
        :param arr: input array
        :return: array of 2 minimal float elements
        """
    min1 = min2 = arr[0]

    for i, item in enumerate(arr):
        if min1 == min2:
            if item < min1:
                min1 = item
        elif item < min1:
            min2 = min1
            min1 = item
        elif item == min1:
            min2 = item
        elif item < min2:
            min2 = item
    result_arr = array('f', [min1, min2])
    return result_arr

TEST_ARRAY1 = array('i', [0, -3, -8, -10, 19, 1, 200])
TEST_ARRAY2 = array('f', [100.0, -12.2, 1.1, -2.2, -1.0, -0.003, -34.0, 12.0])
TEST_ARRAY3 = array('i', [0, 0, 11, 4, 5, 12, 4, 12, 4, 1, 11])
print(get_min(TEST_ARRAY1))
print(get_min(TEST_ARRAY2))
print(get_min(TEST_ARRAY3))
