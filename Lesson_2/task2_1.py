"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""
OPERAND1 = 0.0
OPERAND2 = 0.0
OPERATION = ''
EXITCODE = 0
# internal cycle
while 1:
    if EXITCODE == 1:
        print('Program finished by user request.')
        break
    #  first operand input cycle
    while 1:
        print('\n')
        try:
            OPERAND1 = float(input('Input first operand: '))
            break
        except ValueError:
            print('Enter correct number.')
    #  second operand input cycle
    while 1:
        try:
            OPERAND2 = float(input('Input second operand: '))
            break
        except ValueError:
            print('Enter correct number.')
    while 1:
        OPERATION = (input('Input operation (+,-,*,/): '))
        if OPERATION == '0':
            EXITCODE = 1
            break
        if OPERATION == '+':
            OPERATION = str(OPERAND1) + ' + ' + str(OPERAND2) + ' = '
            print(OPERATION, OPERAND1 + OPERAND2)
            break
        if OPERATION == '-':
            OPERATION = str(OPERAND1) + ' - ' + str(OPERAND2) + ' = '
            print(OPERATION, OPERAND1 - OPERAND2)
            break
        if OPERATION == '*':
            OPERATION = str(OPERAND1) + ' * ' + str(OPERAND2) + ' = '
            print(OPERATION, OPERAND1 * OPERAND2)
            break
        if OPERATION == '/':
            try:
                OPERATION = str(OPERAND1) + ' / ' + str(OPERAND2) + ' = '
                print(OPERATION, OPERAND1 / OPERAND2)
                break
            except ZeroDivisionError:
                print('Devision by zero. Enter other operand or operator.')
                break
        print('Enter correct operator or program stop code (0).')
