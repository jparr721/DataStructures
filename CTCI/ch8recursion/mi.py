"""
magic index is a value whose index is the same as its value
"""

# if value[0] > len(list): return -1


def lin_mi(ls, k):
    if ls[0] > len(ls):
        return -1

    for i, v in enumerate(ls):
        if i == v:
            return i

    return -1


# [-1, 0, 3, 3.1, 4])


def div_mi(ls, k):
    return helper(ls, k, 0, len(ls) - 1)


def helper(ls, k, l, r):
    if l > r:
        return -1

    mid_idx = (l + r) // 2
    mid = ls[mid_idx]

    if mid == mid_idx:
        return mid

    if mid < mid_idx:
        return helper(ls, k, l, mid - 1)
    else:
        return helper(ls, k, mid + 1, r)


if __name__ == "__main__":
    print(lin_mi([-1, 0, 3, 3.1, 4], 4))
    print(div_mi([-1, 0, 3, 3.1, 4], 4))
