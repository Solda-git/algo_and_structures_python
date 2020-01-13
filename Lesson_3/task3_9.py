"""
# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

def get_max_min_item(arr, columns):
    """
        function returns max item of min items of matrix rows
        :param arr: matrix of integer
        :param columns: number of matrix columns integer
        :return: searched item
        """

    l = 0
    while l < columns: #/columns:
        m = 0
        min_item = arr[0][l]
        while m < len(arr):
            if arr[m][l] < min_item:
                min_item = arr[m][l]
            if l == 0:
                result = min_item
            m += 1
        if result < min_item:
            result = min_item
        l += 1
    return result

def print_matrix(arr, columns):
    """
        function prints matrix
        :param arr: matrix of integer
        :param columns: number of matrix columns integer
        :return:
        """
    i = 0
    while i < len(arr):
        j = 0
        while j < columns:
            print(f"[{i}][{j}]", end=': ')
            print(str(arr[i][j]), end='\t\t')
            j += 1
        print()
        i += 1

while True:
    try:
        R_NUMBER = (int(input('Input rows number for matrix: ')))
        C_NUMBER = (int(input('Input columns number for matrix: ')))
        break
    except ValueError:
        print('Input correct integer number.')
#main()
U_MATRIX = []
i = 0
while i < R_NUMBER:
    j = 0
    ROWS = []
    while j < C_NUMBER:
        while True:
            try:
                ROWS.append(int(input(f'Input next element [{i}][{j}]: ')))
                j += 1
                break
            except ValueError:
                print('Input correct integer number.')
    U_MATRIX.append(ROWS)
    i += 1
print_matrix(U_MATRIX, C_NUMBER)
print('Result: ', str(get_max_min_item(U_MATRIX, C_NUMBER)))
