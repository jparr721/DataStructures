# A B C
# A -> All [1, 2, 3, 4, 5]
# return C


C = []


def towers(n):
    if n == 0:
        pass

    towers(n - 1)
    C.append(n)


if __name__ == "__main__":
    print(towers(3))
