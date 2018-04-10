"""
This string counts the letters
in a word and compresses it like:
mom -> m2o1
In this case, since the compressed
word is longer than the original,
the original gets returned
"""


def compress(s):
    compress = {}
    s = s.lower()
    for letter in s:
        count = 0
        if letter in compress:
            count = compress.get(letter)
        compress[letter] = count + 1

    final = ''
    for key, value in compress.items():
        final = ''.join([key + str(value), final])

    return final if len(final) < len(s) else s


print(compress("smiiiiiiiiiile"))
print(compress("applepie"))
