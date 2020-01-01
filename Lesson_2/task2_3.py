"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


def getreversenumber1(nmbr, rvrsd=None):
    """
        doesn't work for numbers containing 0-digits
        function returns reversed value of param - nmbr
        :param nmbr: integer
        :return: integer

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

def getreversenumber(nmbr):
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
    return result

while True:
    try:
        VAL = int(input('Input natural number: '))
        if VAL <= 0:
            print('Enter correct natural number.')
        print('The transformed value of number ', VAL, ' is: ', getreversenumber(VAL))
        break
    except ValueError:
        print('Enter correct natural number.')
        