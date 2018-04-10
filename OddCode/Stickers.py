"""
Given a set of stickets that spell a word,
determine how many stickers you'd need to be
able to cut out enough letters to spell an
entirely different word
"""
import copy
# Reference example: stickerWord = google, word = legolego


def stickers(stickerWord, word):
    ref = {}
    valSum = []

    # Load the string
    for letter in stickerWord:
        count = 0
        if letter in ref:
            count = ref.get(letter)
        ref[letter] = count + 1

    actual = copy.deepcopy(ref)
    for letter in word:
        if letter in actual:
            count = actual.get(letter)
            actual[letter] = count - 1

    for key, value in actual.items():
        if value == 0:
            continue
        compare = ref.get(key)
        valSum.append(abs(value/compare))

    total = 0
    for number in valSum:
        total += number

    return total


print(stickers('google', 'legooooooooooooolego'))
