class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left_ch = None
        self.right_ch = None

def insert_left(self, next_value):
    if self.left_child is None:
        self.left_child = BinaryTree(next_value)
    else:
        new_child = BinaryTree(next_value)
        new_child.left_child = self.left_child
        self.left_child = new_child
    return self

def insert_right(self, next_value):
    if self.right_child is None:
        self.right_child = BinaryTree(next_value)
    else:
        new_child = BinaryTree(next_value)
        new_child.right_child = self.right_child
        self.right_child = new_child
    return self

A_node = BinaryTree('A').insert_left('B').insert_right('C')
print(BinaryTree(A_node))