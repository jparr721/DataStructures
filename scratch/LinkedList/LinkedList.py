class Node(object):

    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:

    head = None
    tail = None

    @property
    def is_empty(self) -> bool:
        return self.head is None

    @property
    def get_size(self) -> int:
        return self.size

    @property
    def get_first(self):
        return self.head.data

    @property
    def get_last(self):
        return self.tail.data

    def insert(self, new_data: any):
        new_node = Node(new_data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def insert_last(self, new_data: any):
        if self.head is None:
            temp = Node(new_data)
            self.head = temp

        self.tail = Node(new_data, self.tail, None)

    def delete_front(self):
        temp = self.head.prev_node
        self.head = temp
        self.head.next_node = None

    def contains(self, value: any) -> bool:
        temp = self.head

        while temp is not None:
            if temp.data is value:
                return True
            temp = temp.next_node
        return False

    def print_elements(self):
        temp = self.head

        while temp is not None:
            if temp.next_node is not None:
                print('{}-->'.format(temp.data), end='')
            else:
                print(f'{temp.data}', end='')

            temp = temp.next_node


def main():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(5)
    ll.insert(10)
    #ll.insert_last(50)
    ll.print_elements()


main()
