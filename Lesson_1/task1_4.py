"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""
from random import random, seed
from datetime import datetime
seed(datetime.now())
MIN = int(input('Input minimum value for integer number: '))
MAX = int(input('Input maximum value for integer number: '))
if MAX < MIN:
    MAX, MIN = MIN, MAX
print('Randomized integer value is: ', str(
    int(random() * (1 + MAX - MIN)) + MIN))
MIN = float(input('Input minimum value for floating point number: '))
MAX = float(input('Input maximum value for floating point number: '))
if MAX < MIN:
    MAX, MIN = MIN, MAX
print('Randomized floating point value is: ',
      str(random() * (MAX - MIN) + MIN))
MIN_CHR = (input('Input first character: '))
MAX_CHR = (input('Input second character: '))
MIN = ord(MIN_CHR)
MAX = ord(MAX_CHR)
print('Randomized character is: ', chr(int(random() * (1 + MAX - MIN)) + MIN))
