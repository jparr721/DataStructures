"""
Create a minimal sized binary
search tree from a sorted array
"""
import math


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def make_bst(tree, l, r):
    if l > r:
        return None

    mid = (l + r) // 2
    n = Node(tree[mid])
    n.left = make_bst(tree, l, mid - 1)
    n.right = make_bst(tree, mid + 1, r)
    return n


def min_bst(arr):
    return make_bst(arr, 0, len(arr) - 1)


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data)
        inorder(node.right)


def min_bst2(ls):
    return make_bst(ls, 0, len(ls) - 1)


def make_bst2(ls, l, r):
    if l > r:
        return None
    mid = ls[math.ceil(len(ls) / 2)]

    root = Node(mid, min_bst2(ls[l:mid]), min_bst2[mid:r])

    return root


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    n = min_bst2(arr)
    inorder(n)
