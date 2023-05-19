def dfs(grid, sr, sc):
    R, C = len(grid), len(grid[0])

    # Base cases
    if not (0 <= sr < R and 0 <= sc < C) or grid[sr][sc] == 0:
        return

    # Mark current cell as visited
    grid[sr][sc] = 0

    # Recursive calls for neighboring cells
    dfs(grid, sr-1, sc)  # Up
    dfs(grid, sr+1, sc)  # Down
    dfs(grid, sr, sc-1)  # Left
    dfs(grid, sr, sc+1)  # Right
