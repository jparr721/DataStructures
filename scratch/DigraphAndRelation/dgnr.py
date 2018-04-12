ground = ['A', 'B', 'C', 'D', 'E']
rel1 = [
        ['A', 'A'], ['A', 'D'],
        ['B', 'C'], ['B', 'D'], ['C', 'E'],
        ['D', 'A'], ['E', 'E']
        ]
ground2 = ['A', 'B', 'C']
rel2 = [
        ['A', 'A'], ['A', 'B'],
        ['A', 'C'], ['B', 'B'], ['B', 'A'],
        ['C', 'C'], ['C', 'A']
        ]
ground3 = ['A', 'B', 'C', 'D']
rel3 = [
        ['A', 'A'], ['A', 'B'],
        ['A', 'C'], ['A', 'D'], ['B', 'D'],
        ['C', 'D'], ['C', 'C']
        ]


def is_reflex(ground, relation):
    """
    This functiont takes the ground set and
    all of the relations of the set and determines
    if there is a reflexive relationship present
    """
    # Match counter set to 0
    matches = 0
    # Run through the ground set to get our compare value
    for current in ground:
        # Count value occurances in the relation
        for rel in relation:
            if rel.count(current) == len(rel):
                matches += 1
    return matches == len(ground)


def is_sym(ground, relation):
    """
    This function takes a ground set
    and a relation and determines if
    there exists a symmetric relationship
    """
    # Set the match counter to 0
    matches = 0
    # Begin iteration through the relations
    for rel in relation:
        # If the first value appears, then we grab and
        # Flip the values and check if they exist
        flipped = []
        flipped.append(rel[1])
        flipped.append(rel[0])
        # For each flipped val check if it exists
        if flipped in relation:
            matches += 1
    # Number of matches should equal the length of the relation
    return matches == len(relation)


def is_antisym(ground, relation):
    """
    This function takes a ground set
    and a relation and determines if there
    exists a symmetric relationship.
    """
    # Iterate through each relation
    for rel in relation:
        flipped = []
        # Flip the values
        flipped.append(rel[1])
        flipped.append(rel[0])
        # If the flipped value exists, but it is
        # not equal to itself, return False
        if flipped in relation and flipped[0] != flipped[1]:
            return False
    return True


def is_trans(ground, relation):
    """
    This function takes a ground set and
    a relation and determines if there
    exists a a transitive relationship
    """
    for rel in relation:
        comp = []



print(is_antisym(ground, rel1))
print(is_antisym(ground2, rel2))
print(is_antisym(ground3, rel3))
