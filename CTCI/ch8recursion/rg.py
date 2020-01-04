"""
robot grid can only go right/down starts in upper left
"""

grid = [[0, 0, 0, 0, 0], [1, 0, 0, 1, 0], [1, 0, 0, 1, 0], [1, 0, 0, 0, 0]]


def move(a, b):
    print(f"moving from pos: {a} to pos: {b}")


def rg(grid):
    total_length = len(grid) * len(grid[1])
    r = 0
    c = 0

    while r < len(grid) - 1 or c < len(grid[0]) - 1:
        if r * c == total_length:
            break

        if c + 1< len(grid[0]) and grid[r][c + 1] != 1:
            move([r, c], [r, c + 1])
            c += 1

        if r + 1 < len(grid) and grid[r + 1][c] != 1:
            move([r, c], [r + 1, c])
            r += 1


if __name__ == "__main__":
    rg(grid)
