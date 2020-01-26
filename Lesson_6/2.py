"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
from  pympler import asizeof
from math import tan
from math import radians


class Polygon:
    def __init__(self, sides_number, height):
        self.sides = sides_number
        self.height = height
        self.side_length = round(2 * tan(radians(360 / self.sides / 2)) * sides_number, 4)

    def get_square(self):
        return round(self.side_length * self.height * self.sides / 2, 4)
    def get_perimetr(self):
        return round(self.sides * self.side_length, 4)

triangle = Polygon(3,8)
quadrate = Polygon(4,4)
octagon = Polygon(8,10)


print(str(quadrate.side_length))
print(str(quadrate.get_square()))
print(str(quadrate.get_perimetr()))


print(str(triangle.side_length))
print(str(triangle.get_square()))
print(str(triangle.get_perimetr()))

print(str(octagon.side_length))
print(str(octagon.get_square()))
print(str(octagon.get_perimetr()))