"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
from random import randint
from timeit import timeit

def bubble_sort(arr):
    """
    Function implements bubble sorting algorithm
    :param arr: array(list} of integer
    :return: returns sorted list of integers
    """

    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1
    return arr

def bubble_sort_optimized(arr):
    """
    Function (optimized) implements bubble sorting algorithm
    :param arr: array(list} of integer
    :return: returns sorted list of integers
    """

    for i in range(0, len(arr) - 1):
        changes = 0
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                changes = 1
            j += 1
        if changes == 0:
            break
        i += 1
    return arr

TEST_ARRAY = []
SIZE = int(input('Input size of int array: '))
for k in range(SIZE):
    TEST_ARRAY.append(randint(-100, 99))
print(TEST_ARRAY)
print(bubble_sort(TEST_ARRAY))

print('Time execution measurement.')
print('Without optimisation.')
CODE_STRING = "bubble_sort(TEST_ARRAY)"
print("t = ", timeit(CODE_STRING, \
setup="from __main__ import bubble_sort, TEST_ARRAY", number=1000))

print('After optimisation.')
CODE_STRING = "bubble_sort_optimized(TEST_ARRAY)"
print("t = ", timeit(CODE_STRING, \
setup="from __main__ import bubble_sort_optimized, TEST_ARRAY", number=1000))
