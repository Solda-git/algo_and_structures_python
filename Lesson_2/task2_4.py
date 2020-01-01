"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

def  getsumofrow(step, rowsum=None):
    """
            function returns sum of row: 1, - 0.5, 0.25, -0.125, ...
            :param step: integer - number of row members
            :return: float

            """
    if step == 1:
        if rowsum is not None:
            return 1 + rowsum
        return 1
    if rowsum is None:
        rowsum = 0
    rowsum += ((-1) ** (step + 1)) / (2 ** (step - 1))
    return  getsumofrow(step - 1, rowsum)

while 1:
    try:
        i = int(input('Input i to define sum of row (\'0\' for exit): '))
        if i == 0:
            break
        if i < 0:
            print('Number must be positive.')
            continue
        print('Sum of row is: ', getsumofrow(i), '\n')

    except ValueError:
        print('Enter correct natural number or \'0\' for exit.')
