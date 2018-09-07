"""
Create a minimal sized binary
search tree from a sorted array
"""


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def min_bst(ar):
    for val in ar:

