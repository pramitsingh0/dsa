def countNegatives(grid):
    m = len(grid)
    n = len(grid[0])
    row = m - 1
    negative_count = 0
    col = 0
    while row >= 0 and col < n:
        if grid[row][col] < 0:
            negative_count += n - col
            row -= 1