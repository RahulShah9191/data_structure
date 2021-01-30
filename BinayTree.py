'''
Created on Mar 22, 2019

@author: Rahul
'''



class Node: 
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
    def print_value(self):
        print(self.data)
    
    def insert(self, data):
        if self.data:
            if self.data > data:
                if self.left_child == None:
                    self.left_child = Node(data)
                else:
                    self.left_child.insert(data)
            else:
                if self.right_child == None:
                    self.right_child = Node(data)
                else:
                    self.right_child.insert(data)                
        else:
            self.data = data
            
    def print_tree(self):
        if self.left_child:
            self.left_child.print_tree()
        print(self.data)
        if self.right_child:
            self.right_child.print_tree()
    
    


root = Node(12)
root.insert(23)
root.insert(10)
root.insert(6)
root.insert(8)
root.insert(20)


root.print_tree()
