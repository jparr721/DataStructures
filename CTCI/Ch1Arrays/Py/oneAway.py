"""
This code checks if the two words have
at most one edit difference between
them.
"""


def oneAway(s1, s2):
    if s1 == s2:
        return True

    longBoy = s1 + s2
    longDict = {}  # lol
    for letter in longBoy:
        count = 0
        if letter in longDict:
            count = longDict.get(letter)
        longDict[letter] = count + 1

    print(longDict)

    diffs = 0
    for count in longDict.values():
        if count < 2:
            diffs += 1

    return diffs < 3


print(oneAway('cake', 'cake'))
print(oneAway('dog', 'fog'))
