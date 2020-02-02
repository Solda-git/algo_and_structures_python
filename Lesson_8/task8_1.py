"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
from collections import Counter

class TreeElement:
    def __init__(self, node_value=None, node_weight=None ):
        self.value = node_value
        self.weight = node_weight
        self.parent = None
        self.left = None
        self.right = None
        #self.index = 0





class Tree:

    def __init__(self, tree_elem):
        self.elems=[]
        self.elems.append(tree_elem)

    def __str__(self):
        result = "Tree: \n"
        for i, item in enumerate(self.elems):
            result = result + f"Item {i}: wiegth = {item.weight}, value = {item.value} \n"
        return result

    def build_branch(self, left_node, right_node):
        if len(self.elems) > 1:
            print('Operation is valir for singe node tree only')
            return self
        self.elems.extend(left_node.elems)
        self.elems.extend(right_node.elems)
        self.elems[0].left = self.elems[1]
        self.elems[0].right = self.elems[len(left_node.elems)+1]
        self.elems[0].weight = left_node.elems[0].weight + right_node.elems[0].weight
        return self



class Haffman:
    """
    Class Haffman intended for coding of strong using Haffman algo
    """
    def __init__(self, input_string):
        self.message_text = input_string
        self.freq_table = Counter(input_string)
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


test = Haffman('beep boop beer!')
print(test.freq_table)

te1 = TreeElement()
te2 = TreeElement('r', 1)
te3= TreeElement('!', 1)
te4= TreeElement('p', 2)
te5 = TreeElement()

tr1 =  Tree(te1)
tr2 =  Tree(te2)
tr3 =  Tree(te3)
tr4 =  Tree(te4)
tr5 =  Tree(te5)

tr1.build_branch(tr2,tr3)
tr5.build_branch(tr1,tr4)

print(tr5)
print(tr5.elems[0].left.right.value)