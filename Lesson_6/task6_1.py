"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

from memory_profiler import profile
import sys


@profile
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

    if len(str(nmbr)) == 1:
        if rvrsd is not None:
            print('Counting references of \'nmbr\' variable.')
            print('nmbr: ', sys.getrefcount(nmbr))
            return rvrsd + nmbr * 10 ** len(str(rvrsd))
        return nmbr
    if rvrsd is None:
        rvrsd = 0
    i = nmbr // (10 ** (len(str(nmbr)) - 1))
    rvrsd = rvrsd + i * (10 ** len(str(rvrsd))) if rvrsd != 0 else i
    return getreversenumber1(nmbr - i * (10**(len(str(nmbr)) - 1)), rvrsd)


@profile
def getreversenumber2(nmbr):
    """
        universal function returns reversed value of param - nmbr
        :param nmbr: integer
        :return: integer
        """
    maxplace = i = len(str(nmbr))
    result = 0
    while i > 0:
        j = nmbr // (10 ** (i - 1))
        result += j * (10 ** (maxplace-i))
        nmbr -= j * (10 ** (i - 1))
        i -= 1
    print('Counting references \'nmbr\' variable.')
    print('nmbr: ', sys.getrefcount(nmbr))
    return result

@profile
def getreversenumber3(nmbr, rvrsd=0):
    """
        universal function returns reversed value of param - nmbr
        using recursion
        :param nmbr: integer
        :param nmbr: integer
        :return: integer
        """
    if nmbr <= 9:
        print('Counting references of \'nmbr\' variable.')
        print('nmbr: ', sys.getrefcount(nmbr))
        return rvrsd*10 + nmbr
    rvrsd = rvrsd * 10 + nmbr % 10
    nmbr = nmbr // 10
    return getreversenumber3(nmbr, rvrsd)

@profile
def getreversenumber4(nmbr):
    """
        universal function returns reversed value of param - nmbr
        using cycle
        :param nmbr: integer
        :param nmbr: integer
        :return: integer
        """
    result = 0
    while nmbr > 0:
        result = result * 10 + nmbr % 10
        nmbr = nmbr // 10
    print('Counting references of \'nmbr\' variable.')
    print('nmbr: ', sys.getrefcount(nmbr))
    return result

TESTNUMBER = 23156123156412345054109

print(sys.getrefcount(TESTNUMBER))

print('Profiling of memory allocation')
print('Function getreversenumber1:\n')
getreversenumber1(TESTNUMBER)
print('____________________________________________________')
print('Function getreversenumber2:\n')
getreversenumber2(TESTNUMBER)
print('____________________________________________________')
print('Function getreversenumber3:\n')
getreversenumber3(TESTNUMBER)
print('____________________________________________________')
print('Function getreversenumber4:\n')
getreversenumber4(TESTNUMBER)
print('____________________________________________________')
print(sys.getrefcount(TESTNUMBER))
