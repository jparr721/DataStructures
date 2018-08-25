class Node(object):
    def __init__(self, data=None, left_node=None, right_node=None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    @property
    def is_empty(self) -> bool:
        return self.root is None

    @property
    def get_root(self) -> Node:
        return self.root

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left_node)
            print(node.data)
            self.inorder(node.right_node)

    def preorder(self, node):
        if node is not None:
            print(node.data)
            self.preorder(node.left_node)
            self.preorder(node.right_node)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left_node)
            self.postorder(node.right_node)
            print(node.data)

    def breadth_first_search(self, value: any) -> bool:
        if self.root is None:
            return False
        queue = [self.root]

        while queue:
            node = queue.pop()
            if node.left_node != value:
                queue.append(node.left_node)
            else:
                print('Value found!')
                return True

            if node.right_node != value:
                queue.append(node.right_value)
            else:
                print('Value found!')
                return True

        print('Value could not be found')
        return False

    def breadth_first_traversal(self):
        queue = [self.root]
        visited = []

        while queue:
            node = queue.pop()
            if node.left_node not in visited:
                visited.append(node.left_node)
                queue.append(node.left_node)
                continue

            if node.right_node not in visited:
                visited.append(node.right_node)
                queue.append(node.right_node)
                continue

        # Print the nodes
        for node in visited:
            print(node.data)

    def insert(self, new_data: any):
        queue = [self.root]

        while queue:
            node = queue.pop()
            if node.left_node is None:
                node.left_node = Node(new_data, None, None)
                return
            else:
                queue.append(node.left_node)

            if node.right_node is None:
                node.right_node = Node(new_data, None, None)
                return
            else:
                queue.append(node.right_node)


def main():
    root_node = Node(1, None, None)
    bt = BinaryTree(root_node)
    bt.insert(4)
    bt.insert(5)
    bt.insert(11)
    bt.inorder(bt.root)


main()
