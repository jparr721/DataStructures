"""
This code checks if the two words have
at most one edit difference between
them.
"""
from collections import defaultdict


def oneAway(s1, s2):
    diff = 0
    if s1 == s2:
        return True

    if len(s1) == len(s2):
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                diff += 1
        if diff > 1:
            return False

    bigString = s1 + s2
    valCounts = defaultdict(int)
    for letter in bigString:
        count = 0
        if letter in valCounts:
            count = valCounts.get(letter)
        valCounts[letter] = count + 1

    for count in valCounts.values():
        if count == 1:
            diff += 1

    return diff > 2


print(oneAway('cake', 'cake'))
print(oneAway('dog', 'fog'))
print(oneAway('bookkeeper', 'bookkeeped'))
print(oneAway('bookkeeper', 'bookkeped'))
