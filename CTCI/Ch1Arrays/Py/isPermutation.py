"""
This checks if one string is a permutation
of another one
"""


def isPermutation(s1, s2):
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))

    if s1 == s2:
        return True
    else:
        return False


print(isPermutation("mom", "mom"))
print(isPermutation("lyonn", "nylon"))
print(isPermutation("Jimmy", "smorvelvius nortrixminie"))
