"""
This algorithm removes dupliactes 
from a Linked List
"""

class Node(object):
    def __init__(self,data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def insert(self, new_data):
        newNode = Node(new_data, self.Head)
        self.head = newNode
        self.size += 1
        

def duplicates(head):
