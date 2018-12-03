# Given a set of numbers {1, 2, 3, 4}
# Find all subsets of that set
# {1}

def power_set(number_set):
    if number_set is None or len(number_set) == 0:
        return set()

    subsets = []
    return get_subsets(number_set, subsets)


def get_subsets(number_set, subsets):

