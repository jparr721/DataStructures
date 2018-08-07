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

    @property
    def print_list(self):
        iterator = self.head

        while iterator is not None:
            print('{}-->'.format(iterator.data), end='')
            iterator = iterator.next_node

    def insert(self, data):
        new_node = Node(None, data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next_node = self.head
        self.head = new_node


def sum_lists(l1, l2):
    list1 = []
    list2 = []
    temp1 = l1.head
    temp2 = l2.head
    while temp1 is not None:
        list1.append(temp1.data)
        temp1 = temp1.next_node
    while temp2 is not None:
        list2.append(temp2.data)
        temp2 = temp2.next_node

    fl1 = ''.join(str(x) for x in list1)
    fl2 = ''.join(str(x) for x in list2)

    total = int(fl1) + int(fl2)
    nl = LinkedList(None)

    for val in str(total):
        nl.insert(val)

    nl.print_list


def main():
    l1 = LinkedList(None)
    l2 = LinkedList(None)
    vals1 = [7, 1, 6]
    vals2 = [5, 9, 2]

    for v in vals1:
        l1.insert(v)

    for v in vals2:
        l2.insert(v)

    l1.print_list
    print('\n')
    l2.print_list

    print('\n')
    sum_lists(l1, l2)


main()
