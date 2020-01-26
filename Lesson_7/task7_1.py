"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
from random import randint

def bubble_sort(arr):
    """
    Function implemets bubble sorting algorithm
    :param arr: array(list} of integer
    :return: returns sorted list of integers
    """

    for i in range(0, len(arr) - 1):
        changes = 0
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
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
