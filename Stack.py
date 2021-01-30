'''
Created on Mar 22, 2019

@author: Rahul
'''

class Stack:
    
    def __init__(self):
        self.data = []
        self.curr_pointer=0
        
    def printStack(self):
        print(self.data)
    
    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False
    
    def push(self, data):
        data[self.curr_pointer] = data
        self.curr_pointer = self.curr_pointer + 1
        
    
    def pop(self):
        if not self.is_empty():
            return self.data[self.curr_pointer]
        return -1

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.printStack()
 
        
        
