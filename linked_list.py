from itertools import count


class Node():
    
    def __init__(self,data):
        self.data = data
        self.next_node = None
        

def __init__(self, root_node_value):
    self.root_node = Node(root_node_value)

def is_empty(self):
    if self.root_node is None:
        return True
    return False 


def print_list(self):
    if not is_empty():
        curr_node = self.root_node
        while curr_node.next_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next_node
    return None


def len(self):
    if not is_empty():
        curr_node = self.root_node
        length =1
        while curr_node.next_node is not None:
            length = length + 1
        return length
    return 0


def get(self,index):
    if not is_empty():        
        curr_nde = self.root_node
        counter=0
        while curr_node.next_node is not None:
            if index is counter:
                return curr_node.data
            curr_node = curr_node.next_node        
    return None


def get_index(self, data):
    if not is_empty():
            curr_nde = self.root_node
            counter=0
            while curr_node.next_node is not None:
                if curr_node.data is data:
                    return counter
                counter = counter + 1
    return None    


def is_exist(self, data):
    if not is_empty(): 
        if get_index(data) is not None:
            return True
    return False

