

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


freq_table = Counter("beep boop beer!")

#freq_table = Counter(input_string)
sorted_elements = deque(sorted(freq_table.items()))
sorted_elements1 = deque(sorted(freq_table.items(), key=lambda item: item[1]))

print(freq_table)

print(sorted_elements)
print(sorted_elements1)



d = deque([1,4,7])
print(str(d[0]))
d.insert(2,2)
print(d)

tr1=Tree(TreeElement(5))
tr2=Tree(TreeElement(10))

d= deque([tr1,tr2])
print (d)
print (d.popleft())

print (d)
