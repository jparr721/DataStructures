def magic_index(l):
    return magic(0, len(l) - 1, l)


def magic(low, high, l):
    if high < low:
        return False, 'fuck'
    mid = (low + high) // 2

    if l[mid] == mid:
        return True, mid
    elif l[mid] > mid:
        return magic(low, mid - 1, l)
    else:
        return magic(mid + 1, high, l)


if __name__ == "__main__":
    l = [-5, 0, 2, 3, 4, 8, 9, 10]
    ll = [-5, 0, 3, 4, 6, 8, 9, 10]

    print(magic_index(l))
    print(magic_index(ll))
