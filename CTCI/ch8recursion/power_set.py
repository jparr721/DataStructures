def power_set(setty_boi: set):
    set_size_2 = len(setty_boi)**2
    s = set()

    for i in range(set_size_2):
        sl = []
        for j in range(len(setty_boi)):
            if i & (1 << j) > 0:
                sl.append(setty_boi[j])
        s.add(tuple(sl))

    return s


if __name__ == "__main__":
    print(power_set([1, 2, 3]))
