"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

def __dec_to_hex__(val):
    result = ""
    while val > 1:
        remainder = val % 16
        if remainder == 10:
            result = "A" + result
        elif remainder == 11:
            result = "B" + result
        elif remainder == 12:
            result = "C" + result
        elif remainder == 13:
            result = "D" + result
        elif remainder == 14:
            result = "E" + result
        elif remainder == 15:
            result = "F" + result
        else:
            result = str(remainder) + result
        val = val // 16
    return result

HEXSET = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", \
          "A", "B", "C", "D", "E", "F"}

class HexNumber:
    """
    Class contains hex value in char collection
    """
    def __init__(self, hex_string):
        self.value = [i for i in hex_string if i in HEXSET]
    def __add__(self, obj):
        return list(__dec_to_hex__(int(''.join(self.value), 16) + int(''.join(obj.value), 16)))
    def __mul__(self, obj):
        return list(__dec_to_hex__(int(''.join(self.value), 16) * int(''.join(obj.value), 16)))

HN1 = HexNumber("A2")
HN2 = HexNumber("C4F")
print(HN1 + HN2)
print(HN1 * HN2)
