class Node(object):
    def __init__(self, data=None, next_node = None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    head = None

    def insert(self, data):
        new_node = Node(data, None)
        if head is None:
            head = new_node
        new_node.next_node = self.head
        self.head = new_node

    def kToLast(self, k):
        checkPtr = self.head
        runner = self.head
        for i in range(0, k):
            checkPtr = checkPtr.next_node

        while checkPtr is not None:
            checkPtr = checkPtr.next_node
            runner = runner.next_node

        return runner
