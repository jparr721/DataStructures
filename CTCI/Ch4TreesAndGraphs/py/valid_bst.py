import random


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


def inorder(root, ls):
    if root is not None:
        inorder(root.left, ls)
        ls.append(root.data)
        inorder(root.right, ls)


def valid_bst(tree):
    ls = []
    inorder(tree, ls)

    return ls == sorted(ls)


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    randomized = random.sample(range(0, 10), 10)
    nodes = min_bst(nodes)

    print(valid_bst(nodes))
    print(valid_bst(min_bst(randomized)))
