"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

class Haffman:
    """
    Class Haffman intended for coding of strong using Haffman algo
    """
    def __init__(self, input_string):
        self.message_text = input_string

    def calc_symbols(self):
        pass


    def build_tree(self):
        pass

    def build_code_tab(self):
        pass

    def encript_message(self):
        pass

    def __str__(self):
        return self.encripted

from collections import Couter

text = input ('Message:')

c = Counter(text)
print(c)
