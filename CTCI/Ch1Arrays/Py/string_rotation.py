"""
Checks if a string is a rotation of
another string
"""

def is_substring(s1, s2):
    return (s1 in s2) or (s2 in s1)

def omni_rotate(l, n):
    return l[-n:] + l[:-n]

def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    if s1 == s2:
        return True

    for i in range(0, len(s1)):
        new_s = omni_rotate(list(s2), i)
        if ''.join(new_s) != s1:
            continue
        else:
            return True
    return False

def string_rotation_option(s1, s2):
    return is_substring((s1 + s1), s2) if len(s1) == len(s2) else False

print(string_rotation('waterbottle', 'erbottlewat'))
print(string_rotation('water', 'rwate'))
print(string_rotation('lala', 'laul'))
print('Other method')
print(string_rotation_option('waterbottle', 'erbottlewat'))
print(string_rotation_option('water', 'rwate'))
print(string_rotation_option('lala', 'laul'))

