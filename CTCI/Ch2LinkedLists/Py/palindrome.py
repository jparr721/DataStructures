class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


def reverse(l):
    return l[::-1]


def LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    @property
    def print_list(self):
        iterator = self.head

        while iterator is not None:
            print('{}-->'.format(iterator.data))
            iterator = iterator.next_node

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next_node = self.head
        self.head = new_node

    @property
    def palindrome(self):
        iterator = self.head
        tl = []
        while iterator is not None:
            tl.append(iterator.data)
            iterator = iterator.next

        compare = reverse(tl)
        return tl == compare


def main():
    ll = LinkedList(None)
    d = [letter for letter in 'racecar']
    print(d)
    for letter in d:
        ll.insert(d)

    print(ll.palindrome)


main()
