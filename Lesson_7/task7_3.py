"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматриваrjyлся на уроках
"""

from statistics import median
from random import randint
from collections import Counter
from timeit import timeit

def find_median(arr):
    """
    function returns median value of an array
    :param arr: array of integers
    :return: returns median value, integer
    """
    if len(arr) == 1:
        return arr[0]
    search_counter = Counter()
    mid = len(arr)//2 # half of array
    for j, item in enumerate(arr):
        search_counter.clear()
        nextloop = 0
        for k, value in enumerate(arr):
            if j == k:
                continue
            if value < item:
                search_counter += (Counter(left=1))
            elif value > item:
                search_counter += (Counter(right=1))
            else:
                search_counter += (Counter(equal=1))
                continue
            if search_counter.most_common(1)[0][1] > mid:
                nextloop = 1
                break
        if nextloop == 0 and \
            abs(search_counter['left']-search_counter['right']) <= search_counter['equal']:
            return item
    return None

def sort_find_median(arr):
    """
    function returns median value of an array, preliminary sorted
    :param arr: array of integers
    :return: returns median value, integer
    """
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
            else:
                continue
    return arr[len(arr)//2]

while 1:
    BASIS = int(input("Input m (0 for escape, 25 - RECOMMENDED): "))
    if BASIS == 0:
        break
    TEST_ARRAY = [randint(0, 100) for i in range(1, 2 * BASIS + 1 + 1)]

    print(TEST_ARRAY)
    print('statistics.median: ', median(TEST_ARRAY))
    CODE_STRING = "median(TEST_ARRAY)"
    print("t = ", timeit(CODE_STRING, \
        setup="from statistics import median; from __main__ import  TEST_ARRAY", number=1000))
    print('sort_find_median: ', sort_find_median(TEST_ARRAY))
    CODE_STRING = "sort_find_median(TEST_ARRAY)"
    print("t = ", timeit(CODE_STRING, \
        setup="from  __main__ import  sort_find_median, TEST_ARRAY", number=1000))
    print('find_median: ', str(find_median(TEST_ARRAY)))
    CODE_STRING = "find_median(TEST_ARRAY)"
    print("t = ", timeit(CODE_STRING, \
        setup="from  __main__ import find_median, TEST_ARRAY", number=1000))
