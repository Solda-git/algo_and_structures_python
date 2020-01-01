"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""
def findsum(number):
    """
            function calculates sum of digits that contains number
            :param number: - integer
            :return: integer - result
            """
    if len(str(number)) == 1:
        return number
    i = number // (10 ** (len(str(number)) - 1))
    return findsum(number - i * (10 ** (len(str(number)) - 1))) + i

while True:
    try:
        RESULT = 0
        MAXSUM = 0
        N = int(input('Input quantity of numbers or 0 for exit: '))
        if N < 0:
            print('Enter correct natural number.')
            continue
        if N == 0:
            break
        while N > 0:
            while True:
                try:
                    NUMBER = int(input('Input number: '))
                    break
                except ValueError:
                    print('Enter correct natural number.')
            if findsum(NUMBER) > MAXSUM:
                MAXSUM = findsum(NUMBER)
                RESULT = NUMBER
            N -= 1
        print('The searched number is: ', RESULT, '( sum = ', MAXSUM, ')')
    except ValueError:
        print('Enter correct natural number.')
