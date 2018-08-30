"""
Given a sorted array, create a minimum
binary search tree
"""


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


root_node = Node(None, None, None)


def insert(root, val):
    if root is None:
        new = Node(val, None, None)
        root = new
    else:
        if root.data < val:
            if root.right is None:
                new = Node(val, None, None)
                root.right = new
            else:
                insert(root.right, val)
        elif root.data > val:
            if root.left is None:
                new = Node(val, None, None)
                root.left = new
            else:
                insert(root.left, val)


def inorder(tree):
    inorder(tree.left)
    print(tree.data)
    inorder(tree.right)


def min_bst(l):
    for v in l:
        insert(root_node, v)

    # print the BST
    inorder(root_node)


item_list = [1, 4, 5, 7, 8, 10, 14, 56, 78]
min_bst(item_list)
