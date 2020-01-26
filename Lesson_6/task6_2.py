"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from math import tan
from math import radians
from pympler import asizeof

class Polygon:
    """
    class Polygon contents:
     parameters of polygon figures:
        - number of sides;
        - height
        - side length 
     and methods:
        - get_square - calculates square of the figure
        - get_perimetr - calculates perimeter of the figure
    """
    def __init__(self, sides_number, height):
        self.sides = sides_number
        self.height = height
        self.side_length = round(2 * tan(radians(360 / self.sides / 2)) * sides_number, 4)

    def get_square(self):
        """
        :return: square of figure
        """
        return round(self.side_length * self.height * self.sides / 2, 4)
    def get_perimeter(self):
        """
        :return: perimeter of figure
        """
        return round(self.sides * self.side_length, 4)

class SlotsPolygon:
    """
        class Polygon contents (protected by __slots__:
         parameters of polygon figures:
            - number of sides;
            - height
            - side length
         and methods:
            - get_square - calculates square of the figure
            - get_perimetr - calculates perimeter of the figure
        """
    __slots__ = ['sides', 'height', 'side_length']
    def __init__(self, sides_number, height):
        self.sides = sides_number
        self.height = height
        self.side_length = round(2 * tan(radians(360 / self.sides / 2)) * sides_number, 4)

    def get_square(self):
        """

        :return:  square of figure
        """
        return round(self.side_length * self.height * self.sides / 2, 4)
    def get_perimeter(self):
        """
        :return: perimeter of figure
        """
        return round(self.sides * self.side_length, 4)


TRIANGLE = Polygon(3, 8)
QUADRATE = SlotsPolygon(4, 4)
OCTAGON = Polygon(8, 10)
SLOTS_OCTAGON = SlotsPolygon(8, 10)


print(f"""Triangle with heigth {TRIANGLE.height} cm has: \
        - length of side: {str(TRIANGLE.side_length)} cm \
        - perimetr: {TRIANGLE.get_perimeter()} cm \
        - square: {TRIANGLE.get_square()} cm^2""")

print(f"""Quadrate with heigth {QUADRATE.height} cm has: \
        - length of side: {str(QUADRATE.side_length)} cm \
        - perimetr: {QUADRATE.get_perimeter()} cm \
        - square: {QUADRATE.get_square()} cm^2""")

print(f"""Octagon with heigth {OCTAGON.height} cm has: \
        - length of side: {str(OCTAGON.side_length)} cm \
        - perimetr: {OCTAGON.get_perimeter()} cm \
        - square: {OCTAGON.get_square()} cm^2""")
print('______________________________')
print(OCTAGON.__dict__)
print(f"Memory used for parameters storage of regular Polygon: \
    {asizeof.asizeof(OCTAGON)} bytes")
print('______________________________')
print(SLOTS_OCTAGON.__slots__)
print(f"Memory used for parameters storage of slots Polygon: \
    {asizeof.asizeof(SLOTS_OCTAGON)} bytes")
