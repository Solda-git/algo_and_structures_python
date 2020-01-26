"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

from random import random
from collections import deque

def merge_sort(arr):
    """
       Function implemets merge sorting algorithm
       :param arr: array(list} of integer
       :return: returns sorted list of integers
       """

    def merge(sorted_arr1, sorted_arr2):
        """
        function merges 2 sorted arrays for merge sorting algorithm
        :param sorted_arr1: array (list) 1 of float items
        :param sorted_arr2: array (list) 2 of float items
        :return: merged array (list) of float items
        """
        deque_1, deque_2 = deque(sorted_arr1), deque(sorted_arr2)
        result = []
        while len(deque_1) > 0 and len(deque_2) > 0:
            if deque_1[0] <= deque_2[0]:
                result.append(deque_1.popleft())
            else:
                result.append(deque_2.popleft())
        if len(deque_1) > 0:
            return result + list(deque_1)
        if len(deque_2) > 0:
            return result + list(deque_2)

    if len(arr) < 2:
        return arr

    return merge(merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:]))

TEST_ARRAY = []
SIZE = int(input('Input size of int array: '))
for k in range(SIZE):
    TEST_ARRAY.append(random()*50.0)
print(TEST_ARRAY)
print(merge_sort(TEST_ARRAY))
