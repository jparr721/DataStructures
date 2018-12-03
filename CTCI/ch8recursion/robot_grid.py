def robot_grid(grid, path):
    for i in range(len(grid) - 1):
        for j in range(len(grid[i]) - 1):
            if grid[i][j+1] == 'x':
                path.append('d')
                print(path)
                return robot_grid(grid[i+1][j], path)
            else:
                path.append('r')
                print(path)
                return robot_grid(grid[i][j+1], path)


def robot_grid_rev(maze):
    if maze is None or len(maze) == 0:
        return None

    path = []
    if get_grid(maze, len(maze) - 1, len(maze[0]) - 1, path):
        return path

    return None


def get_grid(maze, row, column, path):
    if row < 0 or column < 0 or maze is None:
        return False

    atOrigin = row == 0 and column == 0

    if (atOrigin or get_grid(maze, row - 1, column, path) or
            get_grid(maze, row, column - 1, path)):
        path.append(grid[row][column])
        return True
    else:
        return False


grid = [['o', 'x', 'o', 'o'],
        ['o', 'j', 'x', 'o'],
        ['x', 'j', 'j', 'x'],
        ['x', 'x', 'j', 'x'],
        ['x', 'x', 'j', 'j']]

print(robot_grid_rev(grid))
