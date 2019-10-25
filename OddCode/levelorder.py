class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def btree(data):
    return make_btree(data, 0, len(data) - 1)


def make_btree(data, l, r):
    if l > r:
        return None

    m = (l + r) // 2

    node = Node(
        data[m], make_btree(data, l, m - 1), make_btree(data, m + 1, r)
    )
    return node


def inorder(tree):
    if tree is not None:
        print(tree.data)
        inorder(tree.left)
        inorder(tree.right)


def tree_height(tree):
    lv = 0
    ls = []
    make_height(tree, lv, ls, True)

    return ls[-1]


def make_height(tree, lv, ls, jump):
    if tree is not None:
        ls.append(lv)

        if jump:
            lv += 1
            jump = False

        make_height(tree.left, lv + 1, ls, jump)
        make_height(tree.right, lv + 1, ls, jump)


def levelorder(tree):
    mapp = {}
    for i in range(tree_height(tree) + 1):
        lv_help(tree, i, 0, mapp)

    return mapp


def lv_help(tree, lv, count, mapp):
    count += 1
    if tree is None:
        return None

    if lv == 1:
        if count not in mapp:
            mapp[count] = []
        mapp[count].append(tree.data)
        print(f"Level {count}: {tree.data}")
    else:
        lv_help(tree.left, lv - 1, count, mapp)
        lv_help(tree.right, lv - 1, count, mapp)


if __name__ == "__main__":
    tree = btree([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_map = levelorder(tree)
    print(da_map)
