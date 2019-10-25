from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def bftrav(tree):
    q = deque()

    # Add the root node
    q.append(tree)

    while q:
        node = q.pop()
        print(node.data)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right = Node(7)
    root.right.left = Node(6)
    root.right.rught = Node(8)

    bftrav(root)
