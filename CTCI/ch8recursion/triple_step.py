def triple_step(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return (triple_step(n - 3) + triple_step(n - 2) +
                triple_step(n - 1))


def triple_step_dp(n):
    val = [0] * (n + 1)
    val[0] = 1
    val[1] = 1
    val[2] = 2

    for i in range(3, n + 1):
        val[i] = val[i - 1] + val[i - 2] + val[i - 3]

    return val[n]


def triple_step_o1space(n):
    a = 1
    b = 1
    c = 2

    for i in range(3, n + 1):
        d = a + b + c
        a = b
        b = c
        c = d

    return d


print(triple_step(4))
print(triple_step_dp(4))
print(triple_step_o1space(4))
