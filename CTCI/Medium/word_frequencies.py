def word_freq(long_string, word):
    word = word.lower()
    ls = [w.lower().strip() for w in long_string.split()]

    punctuation = ["!", "?", ".", ",", "'", '"']
    start = ['"', "'"]

    dictionary = {}

    for word in ls:
        for p in punctuation:
            if p in word:
                word = word.replace(p, '')
        for s in start:
            if s in word:
                word = word.replace(s, '')

        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary[word]


if __name__ == "__main__":
    print(
        word_freq(
            "hey, my name is jeff and I sure do love! to! exclaim! I!? love to cook, did I mention my name is Jeff?",
            "jeff"))
