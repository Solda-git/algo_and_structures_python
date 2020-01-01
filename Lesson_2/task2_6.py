"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
import sys
from random import random
i = 0
RANDOMVAL = int(random() * 101 - 1)
# to check this task delete comments of next string
# print (RANDOMVAL)
while i < 10:
    #inputmessage = 'Guess the number between 0 and 100. Try N' + i+1
    while True:
        try:
            GUESS = int(input('Guess the number between 0 and 100. Try N' + str(i+1) + ': '))
            if GUESS <= 0 >= 100:
                break
            print('Enter correct number between 1 and 100.')
        except ValueError:
            print('Enter correct number between 1 and 100.')
    if GUESS == RANDOMVAL:
        print('Congrats! You\'ve guessed the number.')
        sys.exit(0)
    if GUESS > RANDOMVAL:
        print('Your number is bigger. ')
    if GUESS < RANDOMVAL:
        print('Your number is less. ')
    i += 1
print('You\'ve lost. The guessed number is:', RANDOMVAL)
