def generate(num_rows: int) -> List[List[int]]:
    if num_rows == 0:
        return []

    base = [[1]]
    if num_rows == 1:
        return base

    if num_rows == 2:
        return [[1], [1, 1]]

    return make_tri([[1], [1, 1]], 2, numRows)

def make_tri(ls, cur_lv, stop):
    end = len(ls) - 1 
    new_level = [1]

    prev = ls[cur_lv - 1] 
    for i in range(0, len(prev)):
        sub = prev[i:i+2]
        if len(sub) > 1:
            rng = sum(prev[i:i+2])
            new_level.append(rng)

    new_level.append(1)
    ls.append(new_level)

    if len(ls) != stop:
        return make_tri(ls, cur_lv + 1, stop)

    return ls
