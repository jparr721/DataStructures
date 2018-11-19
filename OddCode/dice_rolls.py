def dice_helper(n, chosen):
    if n == 0:
        print(chosen)
    else:
        for val in range(6):
            chosen.append(val)
            dice_helper(n - 1, chosen)
            del chosen[len(chosen) - 1]


def dice_sum_helper(n, sum_val, sum_so_far, chosen):
    if sum_so_far == sum_val and len(chosen) == n:
        print(chosen)
    else:
        for val in range(6):
            if sum_so_far + val + 1 * (n - 1) <= sum_val and sum_so_far + val + 6 * (n - 1) >= sum_val:
                chosen.append(val)
                dice_sum_helper(n - 1, sum_val, sum_so_far + val, chosen)
                chosen.pop()

def roll_dice(n):
    '''
    Generate all combinations of
    a pair of a set of n dice
    '''
    chosen = []
    # dice_helper(n, chosen)
    dice_sum_helper(n, 7, 0, chosen)


roll_dice(3)
