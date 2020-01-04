def triple_step(n):
    ls = [None] * (n + 1)
    if n == 0:
        return 1
    if n == 1:
        return 2

    ls[0] = 0
    ls[1] = 1
    ls[2] = 1

    for i in range(3, n + 1):
        ls[i] = ls[i - 1] + ls[i - 2] + ls[i - 3]

    return ls[-1]


if __name__ == "__main__":
    print(triple_step(5))
