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
from memory_profiler import memory_usage
from guppy import hpy

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

h1 = hpy()
m1 = memory_usage()
TESTNUMBER = 23156123156412345054109
print('Profiling of Ffunction \'getreversenumber4\':\n')
getreversenumber4(TESTNUMBER)
print('____________________________________________________')
print('Evaluation of memory usage...')
m2 = memory_usage()
memory_used = m2[0]-m1[0]
print(f'Used {memory_used} MB of memory\n')
print(h1.heap())
