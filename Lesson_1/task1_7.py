"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""

SIDE1 = int(input('Inter side 1 of triangle: '))
SIDE2 = int(input('Inter side 2 of triangle: '))
SIDE3 = int(input('Inter side 3 of triangle: '))
if SIDE1 >= (SIDE2 + SIDE3) or SIDE2 >= (SIDE1 + SIDE3) or SIDE3 >= (SIDE2 + SIDE1):
    print('Such triangle doesn\'t exist.')
if SIDE1 == SIDE2 == SIDE3:
    print('The entered triangle is equilateral.')
elif SIDE1 == SIDE2 or SIDE2 == SIDE3 or SIDE1 == SIDE3:
    print('The entered triangle is isosceles.')
else:
    print('The entered triangle is simple.')
