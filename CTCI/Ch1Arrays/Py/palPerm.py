"""
Checks if a string is a permutation
of a palindrome
"""


def palPerm(string):
    string = string.lower()
    string = string.replace(' ', '')
    matches = {}
    for letter in string:
        count = 0
        if letter in matches:
            print(count)
            count = matches.get(letter)
        matches[letter] = count + 1

    print(matches)

    diffs = 0
    for item in list(matches.values()):
        if item < 2:
            diffs += 1

    return diffs < 2


print(palPerm('Tact Coa'))
