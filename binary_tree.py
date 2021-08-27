class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert_node(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value=value)
                else:
                    self.left.insert_node(value=value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value=value)
                else:
                    self.right.insert_node(value=value)
        else:
            self.value = value

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value, end=" ")
        if self.right:
            self.right.print_tree()

    def is_exist(self, value):
        if self.value == value:
            return True
        elif value < self.value:
            if self.left:
                return False or self.left.is_exist(value)
            else:
                return False
        else:
            if self.right:
                return False or self.right.is_exist(value)
            else:
                return False


import time
root = Node()
for i in range(500,0,-2):
    root.insert_node(i)
for i in range(499,0,-2):
    root.insert_node(i)
root.print_tree()
s = time.perf_counter()
root.is_exist(399)


print(time.perf_counter() - s )
