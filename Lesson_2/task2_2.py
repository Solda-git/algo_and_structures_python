"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""
VAL = 0


def calcevens(nmbr):
    """
        function calculates quantity of even digits of param - numb
        :param nmbr: integer
        :return: integer
        """

    return len(str(nmbr)) - calcodds(nmbr)


def calcodds(nmbr):
    """
        function calculates quantity of odd digits of param - numb
        :param nmbr: integer
        :return: integer
        """

    if len(str(nmbr)) == 1:
        if (nmbr % 2) == 0:
            return 0
        return 1
    i = nmbr // (10**(len(str(nmbr)) - 1))
    quant = 1 if (i % 2) else 0
    return calcodds(nmbr - i * (10**(len(str(nmbr)) - 1))) + quant


while True:
    try:
        VAL = int(input('Input natural number: '))
        if VAL <= 0:
            print('Enter correct natural number.')
        print('Quantity of even digits of number ', VAL, ' is: ', calcevens(VAL))
        print('Quantity of odd digits of number ', VAL, ' is: ', calcodds(VAL))
        break
    except ValueError:
        print('Enter correct natural number.')
