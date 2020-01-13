"""
5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
"""

from array import array

def find_max_negative(arr):
    """
        function returns max negative number from array
        :param arr: array of numbers
        :return: tuple (number, index)
        """
    result_value = 0.0
    result_index = -1
    for i, item in enumerate(arr):
        if (result_value == 0.0) and (item < 0):
            result_value = item
            result_index = i
        elif result_value < item < 0.0:
            result_value = item
            result_index = i
    return (result_value, result_index)

TEST_ARRAY1 = array('f', [0.0, -12.2, 1.1, -2.2, -1.0, -0.003, -34.0, 12.0])
TEST_ARRAY2 = array('i', [0, -3, -8, -10, 19, 1, 200])

print(find_max_negative(TEST_ARRAY1))
print(find_max_negative(TEST_ARRAY2))
