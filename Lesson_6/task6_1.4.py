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

    return result

TESTNUMBER = 23156123156412345054109
print('Profiling of Ffunction \'getreversenumber4\':\n')
getreversenumber4(TESTNUMBER)
print('____________________________________________________')

