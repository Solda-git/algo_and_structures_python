"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

from timeit import Timer
import cProfile

def getreversenumber1(nmbr, rvrsd=None):
    """
        doesn't work for numbers containing 0-digits
        function returns reversed value of param - nmbr
        :param nmbr: integer
        :return: integer

        complexity evaluation:
        recursive function
        O(n) where n = decimal points of number
            n - number of recursion calls
        The slowest algorithm
        """

    if len(str(nmbr)) == 1:                                                 # 1 operation
        if rvrsd is not None:                                               # 1 operation
            return rvrsd + nmbr * 10 ** len(str(rvrsd))                     # 5 operations
        return nmbr                                                         # 1 operation
    if rvrsd is None:                                                       # 1 operation
        rvrsd = 0                                                           # 1 operation
    i = nmbr // (10 ** (len(str(nmbr)) - 1))                                # 5 operations
    rvrsd = rvrsd + i * (10 ** len(str(rvrsd))) if rvrsd != 0 else i        # 6 operations
    return getreversenumber1(nmbr - i * (10**(len(str(nmbr)) - 1)), rvrsd)  # 5 operations




def getreversenumber2(nmbr):
    """
        universal function returns reversed value of param - nmbr
        :param nmbr: integer
        :return: integer

        complexity evaluation:
        T(n) = 5 + n*(4+5+5+2) + 1
        O(n)
        Slow algorithm
        """
    maxplace = i = len(str(nmbr))           # 4 operations
    result = 0                              # 1 operation
    while i > 0:
        j = nmbr // (10 ** (i - 1))         # 4 operations
        result += j * (10 ** (maxplace-i))  # 5 operations
        nmbr -= j * (10 ** (i - 1))         # 5 operations
        i -= 1                              # 2 operations
    return result                           # 1 operation

def getreversenumber3(nmbr, rvrsd=0):
    """
        universal function returns reversed value of param - nmbr
        using recursion
        :param nmbr: integer
        :param nmbr: integer
        :return: integer

        complexity evaluation:
        recursive function
        O(n) where n = decimal points of number
            n - number of recursion calls
        Fast algorithm
        """
    if nmbr <= 9:                               # 1 operation
        return rvrsd*10 + nmbr               # 3 operations
    rvrsd = rvrsd * 10 + nmbr % 10        # 4 operations
    nmbr = nmbr // 10                           # 1 operation
    return getreversenumber3(nmbr, rvrsd)    # 1 operation

def getreversenumber4(nmbr):
    """
        universal function returns reversed value of param - nmbr
        using cycle
        :param nmbr: integer
        :param nmbr: integer
        :return: integer

        complexity evaluation:
        T(n) = 1 + n*(1+4+2) + 1
        O(n)
        The fastest algorithm
        """
    result = 0                               # 1 operation
    while nmbr > 0:                         # 1 operation
        result = result * 10 + nmbr % 10     # 4 operations
        nmbr = nmbr // 10                    # 2 operations
    return result                            # 1 operation

# starting tests

TEST_NUMBER = 12300456123000112341235
TIMEIT_NUMBERS = 10000
REPEAT_NUMBERS = 3
MSG = "Function getreversenumber"

print("1. Running time evaluation with \"Timer.timeit\".\n")

T1 = Timer(f"getreversenumber1({TEST_NUMBER})", "from __main__ import getreversenumber1")
print(f"{MSG}1({MSG}) runs: {T1.timeit(number=TIMEIT_NUMBERS)} ms")

T2 = Timer(f"getreversenumber2({TEST_NUMBER})", "from __main__ import getreversenumber2")
print(f"{MSG}2({TEST_NUMBER}) runs: {T2.timeit(number=TIMEIT_NUMBERS)} ms")

T3 = Timer(f"getreversenumber3({TEST_NUMBER})", "from __main__ import getreversenumber3")
print(f"{MSG}3({TEST_NUMBER}) runs: {T3.timeit(number=TIMEIT_NUMBERS)} ms")

T4 = Timer(f"getreversenumber4({TEST_NUMBER})", "from __main__ import getreversenumber4")
print(f"Function getreversenumber4({TEST_NUMBER}) runs: {T4.timeit(number=TIMEIT_NUMBERS)} ms")

print("\n2. Running time evaluation with \"Timer.timeit\".\n")
print(f"{MSG}1({TEST_NUMBER}) runs:{T1.repeat(repeat = REPEAT_NUMBERS, number=TIMEIT_NUMBERS)} ms")
print(f"{MSG}2({TEST_NUMBER}) runs: {T2.repeat(repeat = REPEAT_NUMBERS, number=TIMEIT_NUMBERS)} ms")
print(f"{MSG}3({TEST_NUMBER}) runs: {T3.repeat(repeat = REPEAT_NUMBERS, number=TIMEIT_NUMBERS)} ms")
print(f"{MSG}4({TEST_NUMBER}) runs: {T4.repeat(repeat = REPEAT_NUMBERS, number=TIMEIT_NUMBERS)} ms")

cProfile.run(f"getreversenumber1({TEST_NUMBER})")