"""
# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).
"""

X = int(input('Input first number: '))
Y = int(input('Input second number: '))
Z = int(input('Input third number: '))
if X == Y or X == Z or Y == Z:
    print('There ar no middle numbers. Some numbers are equal.')
else:
    MID = Y
    if X > MID:
        MID = X
    if MID > Z:
        MID = Z
    print('The mid number is: ', str(MID))
