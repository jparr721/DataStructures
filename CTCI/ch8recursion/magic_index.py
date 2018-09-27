def magic_index(l):
    return magic(l, 0, len(l) - 1)


def magic(l, low, high):
    mid = (low + high) / 2
    if l[mid] == mid:
        return mid
    elif l[mid] > mid:
        magic(l, low, mid)
    else:
        magic(l, mid + 1, high)


def magic_not_distinct(l):
    l = sorted(l)
    for i in range(l):
        if l[i] == 1:
            return i
