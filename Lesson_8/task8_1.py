"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
from collections import Counter, deque

class TreeElement:
    """
    Service class for Tree, provides Tree Node elements
    """
    def __init__(self, node_value=None, node_weight=0):
        self.value = node_value
        self.weight = node_weight
        self.parent = None
        self.left = None
        self.right = None
        #self.index = 0

class Tree:
    """
    Service Class for Haffman class, provides Tree structure for coding
    """
    def __init__(self, tree_elem):
        self.elems = []
        self.elems.append(tree_elem)

    def __str__(self):
        result = "Tree: \n"
        for i, item in enumerate(self.elems):
            result = result + f"Item {i}: wiegth = {item.weight}, value = {item.value} \n"
        return result

    def build_branch(self, left_node, right_node):
        """
        function builds up tree structure using self.node as root,
        left_node as left branch, right_node as right branch
        :param left_node:
        :param right_node:
        :return:
        """
        if len(self.elems) > 1:
            print('Operation is valir for singe node tree only')
            return self
        self.elems.extend(left_node.elems)
        self.elems.extend(right_node.elems)
        self.elems[0].left = self.elems[1]
        self.elems[1].parent = self.elems[0]
        self.elems[0].right = self.elems[len(left_node.elems)+1]
        self.elems[len(left_node.elems) + 1].parent = self.elems[0]
        self.elems[0].weight = left_node.elems[0].weight + right_node.elems[0].weight
        return self

class Haffman:
    """
    Class Haffman intended for coding of strong using Haffman algo
    """
    def __init__(self, input_string):
        self.message_text = input_string
        self.freq_table = Counter(input_string)
        self.code_dict = {}
        self.haffman_tree = Tree(TreeElement())

    def build_tree(self):
        """
        function builds binary tree
        :return: tree link
        """
        # forming of ascending sorted deque of Trees with single node (root)
        # from the symbols frequency table saved in Counter(freq_table)
        tdeque = deque(sorted([Tree(TreeElement(i[0],\
        self.freq_table[i[0]])) for i in self.freq_table], key=lambda x: x.elems[0].weight))
        while len(tdeque) > 2:
            left_tree = tdeque.popleft()
            right_tree = tdeque.popleft()
            new_tree = Tree(TreeElement())
            new_tree.build_branch(left_tree, right_tree)
            for i in range(0, len(tdeque)):
                if  new_tree.elems[0].weight <= tdeque[i].elems[0].weight:
                    tdeque.insert(i, new_tree)
                    break
                if i == len(tdeque)-1:
                    tdeque.append(new_tree)
        left_tree = tdeque.popleft()
        right_tree = tdeque.popleft()
        self.haffman_tree.build_branch(left_tree, right_tree)

    def build_code_tab(self, node=None, code_str=""):
        """
        function builds Haffman code table
        :param node: current tree node
        :param code_str: current code string
        :return: dictionary of  Haffman code table
        """

        #if first call is without 'node' parameter
        if node is None:
            node = self.haffman_tree.elems[0]
        if node.value is not None:
            self.code_dict[node.value] = code_str
        else:
            self.build_code_tab(node.left, code_str + "0")
            self.build_code_tab(node.right, code_str + "1")
        return self.code_dict

    def encrypt_message(self):
        """
        function returns encrypted message
        :return:
        """
        return ''.join([self.code_dict[i] for i in self.message_text])

MY_HAFFMAN = Haffman('beep boop beer!')
MY_HAFFMAN.build_tree()
print("Test message: ", MY_HAFFMAN.message_text)
print("Code table: ", MY_HAFFMAN.build_code_tab())
print("Encripted message: ", MY_HAFFMAN.encrypt_message())
