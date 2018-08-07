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
    def __init__(self, head=None):
        self.head = head

    @property
    def print_list(self):
        temp = self.head
        while temp is not None:
            print('{} -->'.format(temp.data), end='')
            temp = temp.next_node

    def insert(self, data):
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
            return
        new_node.next_node = self.head
        self.head = new_node

    def find(self, item):
        temp = self.head

        while temp is not None:
            if temp.data == item:
                return True
            temp = temp.next_node
        return False


def partition(linked_list, node):
    """Partitions a linked list around a given node"""
    small_list = LinkedList(None)
    big_list = LinkedList(None)

    if linked_list.find(node) is False:
        return False

    temp = linked_list.head

    while temp is not None:
        if temp.data < node:
            small_list.insert(temp.data)
        else:
            big_list.insert(temp.data)
        temp = temp.next_node

    small_list.next_node = big_list
    print('\n')
    small_list.print_list
    print('\n')
    return small_list


def main():
    ll = LinkedList(None)
    ll.insert(3)
    ll.insert(5)
    ll.insert(8)
    ll.insert(5)
    ll.insert(10)
    ll.insert(2)
    ll.insert(1)
    ll.print_list
    new_list = partition(ll, 5)
    print('----------------------------')
    new_list.print_list


main()
