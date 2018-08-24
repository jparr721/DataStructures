"""
This algorithm removes dupliactes
from a Linked List
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    head = None

    @property
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data + '-->', end='')
            temp = temp.next_node

    def insert(self, data):
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
        new_node.next_node = self.head
        self.head = new_node

    def remove(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                temp.next_node = temp.next_node.next_node
            else:
                temp = temp.next_node

    def duplicatesWithBuf(self):
        temp = self.head
        vals = []
        while temp.next is not None:
            if temp.data in vals:
                temp = temp.next_node
            else:
                vals.append(temp.data)
                temp = temp.next_node
        for val in vals:
            print(val + '-->')

    def duplicatesWithoutBuf(self):
        current = self.head
        while current is not None:
            runner = self.head
            while runner is not None:
                if runner.data != current.data:
                    runner.next_node = runner.next_node.next_node
                else:
                    runner = runner.next_node
