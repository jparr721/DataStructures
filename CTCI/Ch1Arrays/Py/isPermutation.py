"""
This checks if one string is a permutation
of another one
"""


def is_permutation(s1, s2):
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))

    return s1 == s2


print(is_permutation("mom", "mom"))
print(is_permutation("lyonn", "nylon"))
print(is_permutation("Jimmy", "smorvelvius nortrixminie"))
