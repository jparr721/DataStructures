def grid_path(r, c, grid):
    # Starting positions
    row = 0
    col = 0
    path = []

    print(f'Using: {r}x{c}')
    while col < c - 1 or row < r - 1:
        if col + 1 < c and grid[row][col + 1] != 'x':
            col += 1
            path.append('right')
        if row + 1 < r and grid[row + 1][col] != 'x':
            row += 1
            path.append('down')

    return path


def p_mat(mat):
    print('\n'.join(
        [''.join(['{:4}'.format(item) for item in row]) for row in mat]))


if __name__ == "__main__":
    grid = [['.', '.', '.', '.'], ['x', '.', '.', '.'], ['.', '.', 'x', '.'],
            ['.', '.', '.', '.'], ['x', '.', '.', '.']]
    p_mat(grid)

    print(grid_path(5, 4, grid))
