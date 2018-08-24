class Node(object):
    def __init__(self, data=None, left_node=None, right_node=None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

class BinaryTree:
    root = None

    @property
    def is_empty(self) -> bool:
        return self.root is None

    @property
    def get_root(self) -> Node:
        return self.root
