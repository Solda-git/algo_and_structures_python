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
            return rvrsd + nmbr * 10 ** len(str(rvrsd))
        return nmbr
    if rvrsd is None:
        rvrsd = 0
    i = nmbr // (10 ** (len(str(nmbr)) - 1))
    rvrsd = rvrsd + i * (10 ** len(str(rvrsd))) if rvrsd != 0 else i
    return getreversenumber1(nmbr - i * (10**(len(str(nmbr)) - 1)), rvrsd)

TESTNUMBER = 23156123156412345054109
print('Function getreversenumber1:\n')
getreversenumber1(TESTNUMBER)
print('____________________________________________________')
