class Node(object):

    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def new_node(self, new_data, new_next, new_prev):
        self.data = new_data
        self.next_node = new_next
        self.prev_node = new_prev


class LinkedList:

    def __init__(self, data=None, head=None, tail=None, size=0):
        self.data = data
        self.head = head
        self.tail = tail
        self.size = size

    def is_empty(self) -> bool:
        return self.head is None

    def get_size(self) -> int:
        return self.size

    def get_first(self):
        return self.head.data

    def get_last(self):
        return self.tail.data

    def insert(self, new_data):
        if self.head is None:
            temp = Node(new_data)
            self.head = temp
            self.head.next_node = None
            self.head.prev_node = None
            self.size += 1
        elif self.size is 1:
            temp = self.head
            new_head = Node(new_data)
            self.tail = self.head
            self.head.next_node = new_head
            self.head = new_head
            self.head.prev_node = temp
            self.size += 1
        else:
            temp = self.head
            new_head = Node(new_data)
            self.head.next_node = new_head
            self.head = new_head
            self.head.prev_node = temp
            self.size += 1

    def insert_last(self, new_data):
        if self.head is None:
            temp = Node(new_data)
            self.head = temp

        self.tail = Node(new_data, self.tail, None)

    def delete_front(self):
        temp = self.head.prev_node
        self.head = temp
        self.head.next_node = None

    def contains(self, value) -> bool:
        temp = self.head

        while(temp is not None):
            if temp.data is value:
                return True
            else:
                temp = temp.next_node
        return False

    def print_elements(self):
        temp = self.tail

        while(temp is not None):
            if temp.next_node is not None:
                print('%d-->' % temp.data, end='')
            else:
                print('%d' % temp.data, end='')
            temp = temp.next_node


def main():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(5)
    ll.insert(10)
    ll.insert_last(50)
    ll.delete_front()
    ll.print_elements()


main()
