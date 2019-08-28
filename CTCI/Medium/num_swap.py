def swap(p1, p2, a):
    a[p2], a[p1] = a[p1], a[p2]
    return a


if __name__ == "__main__":
    ls = [1, 2, 3, 4, 5]
    print(swap(0, 3, ls))
