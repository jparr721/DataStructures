"""
Partitions a list around a value X
such that all values less than X are
on the left side of the partition and
all values >= X are on the right side of
the partition
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList(object):
    head = None

    @property
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next_node

    def insert(self, data):
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
            return
        new_node.next_node = self.head
        self.head = new_node



