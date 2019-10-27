"""
Calculates the determinant via the laplace expansion
"""


def det(A):
    dets = []
    coeffs = {}
    det_helper(A, coeffs, dets)

    for k, v in coeffs.items():
        dets[k] = multiply_each(dets[k], v)
    return formulate(dets)


def formulate(ls):
    total = ls[0]
    neg = True
    for i in range(1, len(ls)):
        if neg:
            total -= ls[i]
            neg = False
        else:
            total += ls[i]
            neg = True

    return total


def multiply_each(v, ls):
    for i in ls:
        v *= i

    return v


def safe_add(coeefs, key, value):
    if key not in coeefs:
        coeefs[key] = []

    coeefs[key].append(value)

    return coeefs


def construct_intermediate_mat(small_mat, bad_col_idx):
    new_mat = []
    for row in small_mat:
        new_mat.append([*row[0:bad_col_idx], *row[bad_col_idx + 1:]])

    return new_mat


def remove_top(mat):
    new_mat = []

    for i in range(1, len(mat)):
        new_mat.append(mat[i])

    return new_mat


def p(A):
    string = "[\n"
    for l in A:
        string += f"{repr(l)}\n"

    string += "]\n"

    return string


def det_helper(A, coeffs, dets):
    print(p(A))
    if len(A) == 2:
        det = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
        # print("
        dets.append(det)
        return None

    top_row = A[0]
    for i, coef in enumerate(top_row):
        coeffs = safe_add(coeffs, i, coef)
        new_mat = construct_intermediate_mat(remove_top(A), i)
        det_helper(new_mat, coeffs, dets)


if __name__ == "__main__":
    # print(det([[1, 2, 3], [2, 1, 3], [3, 2, 1]]))
    print(det([[1, 2, 3, 4], [2, 1, 3, 4], [3, 2, 1, 4], [4, 3, 2, 1]]))
