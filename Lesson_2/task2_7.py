"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""

def calcleft(n_param):
    """
            function calculates summary of row 1+2+...+n
            :param n: integer - number of row memebers
            :return: integer - summary
            """
    if n_param == 1:
        return 1
    return n_param+calcleft(n_param-1)

def calcright(n_param):
    """
            function calculates n(n+1)/2
            :param n: integer
            :return: integer
            """
    return int(n_param*(n_param+1)/2)

print('Let\'s prove the folowing equation for natural n: ')
print('1 + 2 + ... + n = n * (n + 1) / 2')

while True:
    try:
        N = int(input('Input natural n or 0 for exit: '))
        if N < 0:
            print('Enter correct natural number.')
            continue
        if N == 0:
            break
        print('Calculate left part of equation for n = ', N)
        print('1 + 2 + ... + n = ', calcleft(N))
        print('Calculate right part of equation for n = ', N)
        print('n * (n + 1) / 2 = ', calcright(N))
        if calcleft(N) == calcright(N):
            print('For neutral n = ', N, ': 1 + 2 + ... + n = n * (n + 1) / 2')
            print(calcleft(N), ' = ', calcright(N))
        else:
            print('Equation is not true')
        input()
    except ValueError:
        print('Enter correct natural number.')
