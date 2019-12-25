"""
# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

"""
NUMBER = input('Input position number of character: ')
if not NUMBER.isdigit():
    print('Enter correct value between 1 and 26. Try again')
else:
    if int(NUMBER) < 1 or int(NUMBER) > 26:
        print('Enter correct value between 1 and 26. Try again')
    else:
        print('The requested character is:', chr(int(NUMBER)+96))
