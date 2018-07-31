"""
This replaces all spaces in strings
with %20 like it's a URL
"""


def urlify(string):
    string = string.strip().split(' ')
    string = '%20'.join(string)
    print(string)


urlify('Mr John Smith')
urlify('Mr      John     Smith   ')
