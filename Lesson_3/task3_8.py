"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

R_NUMBER = 4
C_NUMBER = 5

R_MATRIX = []
i = 0

while i < R_NUMBER:
    SUMROW = 0
    C_MATRIX = []
    j = 0
    while j < C_NUMBER - 1:
        while True:
            try:
                C_MATRIX.append(int(input(f'Input next element [{i}][{j}]: ')))
                break
            except ValueError:
                print('Input correct integer number.')
        SUMROW += C_MATRIX[j]
        j += 1
    C_MATRIX.append(SUMROW)
    R_MATRIX.append(C_MATRIX)
    i += 1
i = 0

while i < R_NUMBER:
    j = 0
    while j < C_NUMBER:
        print(str(R_MATRIX[i][j]), end='\t\t')
        j += 1
    print()
    i += 1
