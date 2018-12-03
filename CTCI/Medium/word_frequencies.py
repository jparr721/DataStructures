def word_frequencies(string_of_text):
    '''Take the words in a big string of
    text and get the count of each'''

    counts = {}

    for s in string_of_text.split(' '):
        s = s.lower().strip()

        if s in counts:
            counts[s] += 1
        else:
            counts[s] = 1

    return counts


def get_word_count(word, counts):
    print(counts)
    return counts[word]


long_as_shit = 'hello my name is jeff. I love to eat oranges and apples and my name is jeff oh yeah'

counts = word_frequencies(long_as_shit)
print(get_word_count('jeff', counts))
print(get_word_count('i', counts))

