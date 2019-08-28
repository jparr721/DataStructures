from sys import argv


def n_steps(n, memo):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    elif memo[n] is None:
        memo[n] = n_steps(n - 1, memo) + n_steps(n - 2, memo) + n_steps(
            n - 3, memo)
        return memo[n]
    else:
        return memo[n]


def triple_step(n):
    ar = [None for i in range(n + 1)]
    return n_steps(n, ar)


if __name__ == "__main__":
    print(triple_step(int(argv[1])))
