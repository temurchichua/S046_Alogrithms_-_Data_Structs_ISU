from collections import deque


def bfs(grid, sr, sc):
    R, C = len(grid), len(grid[0])

    # Define the directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Create a queue for BFS traversal
    queue = deque([(sr, sc)])

    # Mark the starting cell as visited
    grid[sr][sc] = 0

    while queue:
        # Process the front cell in the queue
        curr_row, curr_col = queue.popleft()

        # Explore neighbors
        for dr, dc in directions:
            next_row, next_col = curr_row + dr, curr_col + dc

            # Check if the neighbor is valid and unvisited
            if 0 <= next_row < R and 0 <= next_col < C and grid[next_row][next_col] == 1:
                # Mark the neighbor as visited
                grid[next_row][next_col] = 0
                # Add the neighbor to the queue for further exploration
                queue.append((next_row, next_col))
