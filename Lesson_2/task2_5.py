"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

MINCODE = 32
MAXCODE = 127
COLUMNS = 10

CHRMATRIX = ''
i = MINCODE
while i <= MAXCODE:
    CHRMATRIX += str(i) + ': ' + chr(i) + '\t'
    if (i - MINCODE + 1) % COLUMNS == 0:
        CHRMATRIX += '\n'
    i += 1
print(CHRMATRIX)
