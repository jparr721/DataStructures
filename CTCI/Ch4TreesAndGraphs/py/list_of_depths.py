class LinkedListNode(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class TreeNode(object):
    def __init__(self, data=None, left_node=None, right_node=None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = LinkedListNode(data, None)
        if self.head is None:
            self.head = data
        else:
            self.head.next_node = new_node
            self.head = new_node


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        queue = [self.root]

        while queue:
            node = queue.pop()
            if node.left_node is None:
                node.left_node = TreeNode(data, None, None)
                return
            else:
                queue.append(node.left_node)

            if node.right_node is None:
                node.right_node = TreeNode(data, None, None)
                return
            else:
                queue.append(node.right_node)


def height(root):
    '''
    Helper to get tree height
    '''
    height = 0
    if root is None:
        return 0
    else:
        left_height = height(root.left_node)
        right_height = height(root.right_node)

        height = left_height if left_height > right_height else right_height

        return height


def add_level_nodes(root, level):
    if root is None:
        return
    if level == 1:
        ll = LinkedList()
        ll.insert(root.data)
        return ll
    elif level > 1:
        add_level_nodes(root.left, level - 1)
        add_level_nodes(root.right, level - 1)


def list_of_depths(root):
    tree_height = height(root)
    list_of_lists = []

    for i in range(tree_height + 1):
        list_of_lists.append(add_level_nodes(root, i))
