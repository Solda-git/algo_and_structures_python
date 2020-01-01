"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""

def calc_digit_quant(digit, number):
    """
                function calculates quantity digit entries in number
                :param digit: searching digit in number
                :param number: searching digit in number
                :return: integer - quantity
                """
    if len(str(number)) == 1:
        if number == digit:
            return 1
        return 0
    i = number // (10 ** (len(str(number)) - 1))
    newnumber = number - i * (10 ** (len(str(number)) - 1))
    # zeros check:
    if (len(str(number)) - len(str(newnumber)) > 1) & (digit == 0):
        quant = len(str(number)) - len(str(newnumber)) - 1
    else:
        quant = 1 if (i == digit) else 0
    return calc_digit_quant(digit, newnumber) + quant

while True:
    try:
        RESULT = 0
        N = int(input('Input quantity of numbers or 0 for exit: '))
        if N < 0:
            print('Enter correct natural number.')
            continue
        if N == 0:
            break
        while True:
            try:
                DIGIT = int(input('Input digit to calculate: '))
                if len(str(DIGIT)) > 1:
                    print('You need to enter only one digit symbol (0-9). Try again.')
                    continue
                break
            except ValueError:
                print('Enter correct natural number.')
        while N > 0:
            while True:
                try:
                    NUMBER = int(input('Input number: '))
                    break
                except ValueError:
                    print('Enter correct natural number.')
            RESULT += calc_digit_quant(DIGIT, NUMBER)
            N -= 1
        print('Quantity of digit <', DIGIT, '> entries in numbers: ', str(RESULT))
        input()
    except ValueError:
        print('Enter correct natural number.')
