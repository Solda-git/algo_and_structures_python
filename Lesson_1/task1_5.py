"""
#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.
"""

CHAR1 = input('Input first character: ')
CHAR2 = input('Input second character: ')
if (len(CHAR1) != 1 or len(CHAR2) != 1 or CHAR1 == CHAR2):
    print('Enter correct different characters. try again.')
else:
    print('Position of character 1 is: ', str(ord(CHAR1)-96))
    print('Position of character 2 is: ', str(ord(CHAR2)-96))
    if ord(CHAR1) > ord(CHAR2):
        CHAR1, CHAR2 = CHAR2, CHAR1
    OUTPUT = 'There are ' + str(ord(CHAR2) - ord(CHAR1) - 1)
    OUTPUT = OUTPUT + ' character(s) between first and second entered character'
    print(OUTPUT)
