"""
8.	Определить, является ли год, который ввел пользователем,
# високосным или не високосным.
 Год является високосным в двух случаях: либо он кратен 4,
# но при этом не кратен 100, либо кратен 400.

"""

YEAR = input('Input year: ')
if not YEAR.isdigit():
    print('Enter correct year')
elif len(YEAR) != 4:
    print('Enter correct year')
else:
    if (not int(YEAR) % 4 and (int(YEAR) % 100)) or (not int(YEAR) % 400):
        print('this is leap year')
    else:
        print('this is not leap year')
