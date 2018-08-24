import sys


def diff_array(s1, s2):
    #  First try, brute force
    max_diff = sys.maxsize
    nums = []
    for val in s1:
        for val2 in s2:
            if abs(val - val2) < max_diff:
                nums = [val, val2]
                max_diff = abs(val - val2)

    return nums

def dif_array(ar1, ar2):



print(diff_array([1, 5, 10, 900], [9, 8, 14, 11]))
