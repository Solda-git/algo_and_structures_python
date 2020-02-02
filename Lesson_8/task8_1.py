"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
from collections import Counter, deque

class TreeElement:
    def __init__(self, node_value=None, node_weight=0):
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

    #def __mod__(self):
    #    return self[0].weight

    def build_branch(self, left_node, right_node):
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
        #serv_deque = deque(sorted(self.freq_table.items(), key = lambda i: i[1]))
        #print(serv_deque)

    def build_tree(self):
        # forming of ascending sorted deque of Trees with single node (root)
        # from the symbols frequency table saved in Counter(freq_table)
        tdeque = deque(sorted([Tree(TreeElement(i[0], self.freq_table[i[0]])) for i in self.freq_table], key=lambda x: x.elems[0].weight))
        while len(tdeque) > 2:
            print(f"len(tdeque): {len(tdeque)}")
            left_tree = tdeque.popleft()
            print(left_tree)
            right_tree = tdeque.popleft()
            new_tree = Tree(TreeElement())
            new_tree.build_branch(left_tree, right_tree)
            for i in range(0, len(tdeque)):
                if  new_tree.elems[0].weight <= tdeque[i].elems[0].weight:
                    tdeque.insert(i, new_tree)
                    break
                if i == len(tdeque)-1:
                    tdeque.append(new_tree)
        self.haffman_tree = Tree(TreeElement())
        left_tree = tdeque.popleft()
        right_tree = tdeque.popleft()
        self.haffman_tree.build_branch(left_tree, right_tree)

    def build_code_tab(self, node = None, code_str=""):

        """ for i, item in enumerate(self.haffman_tree.elems):
            if item.value is not None:
                reverse_code=''
                while item.parent is not None:
                    if item.parent.left == item:
                        reverse_code += '0'
                    else:
                        reverse_code += '1'
                self.code_dict[item.value] = reverse_code.reverse()
        """
        #if first call without 'node' parameter
        if node is None:
            node = self.haffman_tree.elems[0]
        if node.value is not None:
            self.code_dict[node.value] = code_str
        else:
            self.build_code_tab(node.left, code_str + "0")
            self.build_code_tab(node.right, code_str + "1")
        return self.code_dict

    def encript_message(self):
        pass

    def __str__(self):
        return self.encripted


test = Haffman('beep boop beer!')
test.build_tree()
print(test.build_code_tab())


## formed tree testing


print(str(test.haffman_tree.elems[0].left.left.value))
print("!!! ", str(test.haffman_tree.elems[0].left.right.right.value), " !!!")

print(str(test.haffman_tree.elems[0].right.right.value))
print(str(test.haffman_tree.elems[0].right.left.left.right.value))

#print(test.freq_table)
"""
tr1 =  Tree(TreeElement())
tr2 =  Tree(TreeElement('r', 1))
tr3 =  Tree(TreeElement('!', 1))
tr4 =  Tree(TreeElement('p', 2))
tr5 =  Tree(TreeElement())

tr1.build_branch(tr2,tr3)
tr5.build_branch(tr1,tr4)

print(tr5)
print(tr5.elems[0].left.right.value)
#freq_table = Counter("beep boop beer!")
#list = [freq_table[i[0]] for i in freq_table ]
#tlist = deque([Tree(TreeElement(i[0],freq_table[i[0]])) for i in freq_table ])

#tlist = deque(sorted([Tree(TreeElement(i[0],freq_table[i[0]])) for i in freq_table], key=lambda x: x.elems[0].weight))

#sorted("beep boop beer!")

#print(freq_table)
#print(f"Первый символ: {tlist[0].elems[0].value}, частота: {tlist[0].elems[0].weight}.")
#print(f"Последний символ: {tlist[len(tlist)-1].elems[0].value}, частота: {tlist[len(tlist)-1].elems[0].weight}.")
"""