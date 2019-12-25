"""
lesson1
Task1: Finding sum and multiplication of digits of three digit number
"""

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
VAL = int(input('Input three-digit number: '))
DIGIT1 = VAL//100
DIGIT2 = (VAL - DIGIT1*100)//10
DIGIT3 = VAL - DIGIT1*100 - DIGIT2*10
print('Sum of digits: ', DIGIT1+DIGIT2+DIGIT3, 'multiplication of digits: ', DIGIT1*DIGIT2*DIGIT3)
