class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    head = None

    def insert(self, data):
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def deleteMid(self, mid):
        mid.data = mid.next_node.data
        mid.next_node = mid.next_node.next_node

    def print_elements(self):
        temp = self.head

        while (temp):
            if temp.next_node is not None:
                print('{}-->'.format(temp.data), end='')
            else:
                print(f'{temp.data}', end='')

            temp = temp.next_node


def main():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(10)
    ll.insert(20)
    ll.insert(100)
    ll.print_elements()
    print('\n')
    h = ll.head.next_node
    print('{} \n'.format(h.data))
    ll.deleteMid(h)
    ll.print_elements()


main()
