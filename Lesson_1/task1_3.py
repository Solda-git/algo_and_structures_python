"""
lesson1
Task3: finding of line equation like y = kx + b
crossing of two points (x,y)
"""

# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.
X1 = float(input('Iput x1 value: '))
Y1 = float(input('Iput y1 value: '))
X2 = float(input('Iput x2 value: '))
Y2 = float(input('Iput y2 value: '))
K = (Y1-Y2)/(X1-X2)
B = Y1 - K*X1
if K == 1:
    if B > 0:
        print('The equations of line is: y = x + ', B)
    elif B == 0:
        print('The equations of line is: y = x')
    else:
        print('The equations of line is: y = x - ', -B)
elif  K == -1:
    if B > 0:
        print('The equations of line is: y = -x + ', B)
    elif B == 0:
        print('The equations of line is: y = -x')
    else:
        print('The equations of line is: y = -x - ', -B)
else:
    if B > 0:
        print('The equations of line is: y = ', K, 'x + ', B)
    elif B == 0:
        print('The equations of line is: y = ', K, 'x')
    else:
        print('The equations of line is: y = ', K, 'x - ', -B)
