"""
Given two linked lists of numbers
sum them and print the result
as another linked list
"""

class Node(object):
    def __init__(self, next_node=None, data=None):
        self.next_node = next_node
        self.data = data


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(None, data)
        if self.head is None:
            self.head = new_node

def sum_lists()
