from typing import List


def swap(ls, p1, p2):
    ls[p1], ls[p2] = ls[p2], ls[p1]
    return ls


def insertion_sort(ls: List[int]):
    for i in range(1, len(ls)):
        v = ls[i]
        j = i - 1
        while j >= 0 and v < ls[j]:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = v
    return ls


if __name__ == "__main__":
    ls = [5, 4, 3, 6, 12, 24, 1]
    ls = insertion_sort(ls)

    print(ls)
