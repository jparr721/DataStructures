def small_dif(l1, l2):
    l1 = sorted(l1)
    l2 = sorted(l2)

    p1 = 0
    p2 = 0
    smallest = 2**40

    while p1 < len(l1) or p2 < len(l2):
        diff = l1[p1] - l2[p2]
        print(diff, len(l1), len(l2), p1, p2)
        if diff >= 0 and diff < smallest:
            smallest = diff
        elif diff < 0 and len(l1) - 1 >= p1:
            p1 += 1
        else:
            if len(l2) - 1 >= p2:
                p2 += 1

    return smallest


if __name__ == "__main__":
    l1 = [1, 3, 15, 11, 2]
    l2 = [23, 127, 235, 19, 8]

    print(small_dif(l1, l2))
