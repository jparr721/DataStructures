"""
This checks if a word contains
all unique letters.
"""


def isUnique(word):
    wordList = []
    for letter in word:
        if letter in wordList:
            return False
        else:
            wordList.append(letter)
    return True


print(isUnique("turtle"))
print(isUnique("Libre"))
