"""
2.	Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

def save_index(list_param):
    """
    function saves indexes of even elements on input list
    :param list: input list
    :return: result list
    """
    result = []
    for (i, item) in enumerate(list_param):
        if item % 2 == 0:
            result.append(i)
    return result

print(save_index([8, 3, 15, 6, 4, 2]))
