def exchange(matrix, i, j):
    matrix[i], matrix[i] = matrix[i], matrix[j]


def scale(matrix, row, factor):
    for i in range(len(matrix[row])):
        matrix[row][i] *= factor


def rowreplacement(matrix, i, j, factor):
    for k in range(len(matrix[j])):
        matrix[j][k] += matrix[i][k] * factor


def rowreduce(matrix):
    n = len(matrix)

    # find pivot and make zeroes below diagonal in each column
    for i in range(n):
        # find pivot
        for j in range(i, n):
            if matrix[j][i] != 0:
                if i != j:
                    exchange(matrix, i, j)
                break
            if j == n - 1:
                print(f"No pivot in column {str[i]}")
                import sys

                sys.exit(1)

        # put zeroes below diagonal
        for j in range(i + 1, n):
            rowreplacement(matrix, i, j, -matrix[j][i] / float(matrix[i][i]))

    # back substitution
    for i in range(n - 1, 0, -1):
        for j in range(i):
            rowreplacement(matrix, i, j, -matrix[j][i] / float(matrix[i][i]))

    # put 1's on diagonal
    for i in range(n):
        scale(matrix, i, 1 / float(matrix[i][i]))


def p(A):
    string = "[\n"
    for l in A:
        string += f"{repr(l)}\n"

    string += "]\n"

    return string


if __name__ == "__main__":
    matrix = [[1, 2, 1], [2, 1, 2]]
    print(f"Starter:\n{p(matrix)}")
    rowreduce(matrix)
    print(p(matrix))
