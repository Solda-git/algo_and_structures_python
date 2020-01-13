"""
1.	В диапазоне натуральных чисел от 2 до 99 определить,
 сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

def print_dividers(ch_range, d_range):
    """
    :param checkRange: list to be checked for deviders
    :param divRange: list of deviders
    :return: return list of number of multiples
    """
    result = []
    for i in d_range:
        temp_list = []
        for j in range(i, ch_range[len(ch_range) - 1] + 1, i):
            temp_list.append(j)
        print(f"Number of dividers for {i} in range [{MIN}, {MAX}]: {len(temp_list)}")
        result.append(len(temp_list))
    return result

MIN = 2
MAX = 99
MINDIV = 2
MAXDIV = 9

CHECK_RANGE = [x + MIN for x in range(0, MAX - 1)]
DIV_RANGE = [x + MINDIV for x in range(0, MAXDIV - 1)]
print(print_dividers(CHECK_RANGE, DIV_RANGE))
