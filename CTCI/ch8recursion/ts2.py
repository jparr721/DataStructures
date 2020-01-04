"""
Child is running up a staircase with n steps, it can go up 1 2 or 3 steps
How many possible ways are there
"""

#       ____
#    ___
# __


def triple_step(n):
    ls = [0 for i in range(n + 1)]
    ls[0] = 0
    ls[1] = 1
    ls[2] = 2

    for i in range(3, n + 1):
        ls[i] = ls[n - 1] + ls[n - 2] + ls[n - 3]

    return ls[-1]


def triple_step_no_mem(n):
    a = 0
    b = 1
    c = 2
    d = 0

    for i in range(3, n):
        d = a + b + c
        a = b
        b = c
        c = d

    return a + b + c


if __name__ == "__main__":
    print(triple_step(5))
    print(triple_step_no_mem(5))
