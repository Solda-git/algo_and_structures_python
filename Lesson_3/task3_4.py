"""
# 4.	Определить, какое число в массиве встречается чаще всего.
"""
def get_max_count_item(list_param):
    """
    function returns the most frequent item of the list
    :param list_param: input list
    :return: integer
    """
    tmp_dict = {}
    max_freq = 1
    result = 0
    for (i, item) in enumerate(list_param):
        if item in tmp_dict:
            tmp_dict[item] += 1
        else:
            tmp_dict[item] = 1
    for (i, item) in enumerate(tmp_dict):
        print(f"index = {i}, item = {item}, tmp_dict[item] = {tmp_dict[item]}")
        if tmp_dict[item] > max_freq:
            max_freq = tmp_dict[item]
            result = item
    return result

print(str(get_max_count_item([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 2, 2, 2, 3, 3, 3, 3])))
print(str(get_max_count_item([-7, 1, 5, 3, 7, -6, 1, 0, 0, 2, -7, 0])))
