def dice_helper(n, chosen):
    if n == 0:
        print(chosen)
    else:
        for val in range(6):
            chosen.append(val)
            dice_helper(n - 1, chosen)
            del chosen[len(chosen) - 1]


def roll_dice(n):
    '''
    Generate all combinations of
    a pair of a set of n dice
    '''
    chosen = []
    dice_helper(n, chosen)


roll_dice(3)
