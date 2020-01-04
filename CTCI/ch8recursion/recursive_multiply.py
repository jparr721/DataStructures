import math


def recursive_multiply(a, b):
    if b % 2 == 0:
        return a << math.floor(b / 4)

    return (a << math.floor(b / 4)) + a


if __name__ == "__main__":
    print(recursive_multiply(2, 2))
