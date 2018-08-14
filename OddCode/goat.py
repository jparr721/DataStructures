# Goat latin 
# If a word begins with a consonant, remove the first letter
# append it to the end and add 'ma'.
# If it begins with a vowel then append ma to the end of the word
# Add an a to end the of the word based on the index starting with 1

def goat_latin(in_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = in_str.split(' ')

    for i in range(len(words)):
        if words[i][0] not in vowels:
            old_char = words[i][0]
            new_word = words[i].replace(words[i][0], '')
            new_word = new_word + old_char + 'ma' 
            words[i] = new_word
        else:
            new_word = word + 'ma'
            words[i] = new_word

    for i in range(len(words)):
        numA = i + 1
        words[i] = words[i] + 'a'*numA

    final = ' '.join(words)
    return final

print(goat_latin('I speak goat latin'))
