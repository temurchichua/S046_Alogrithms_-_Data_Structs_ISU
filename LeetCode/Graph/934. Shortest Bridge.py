class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)  # it's n x n matrix
        queue = deque()  # prepare list for BFS

        directions = [(-1, 0), (1, 0),  # up, down
                      (0, -1), (0, 1)]  # left, right

        def dfs(x, y):
            grid[x][y] = 2
            queue.append((x, y))  # We can BFS from that node in future

            for _x, _y in directions:
                _x += x
                _y += y
                # if new address is within the range of graph and island is 1
                if 0 <= _x < n and 0 <= _y < n and grid[_x][_y] == 1:
                    dfs(_x, _y)

        def mark_second_island():
            """both islands are valued 1. Just change the first island values to 2 """
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        dfs(i, j)
                        return

        # - DFS find all nodes in first island and turn it into 2
        mark_second_island()

        # - BFS to find the shortest path from island A to island B
        distance = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for _x, _y in directions:
                    _x += x
                    _y += y
                    # if new address is within the range of graph and island is 1
                    if 0 <= _x < n and 0 <= _y < n:
                        if grid[_x][_y] == 1:
                            return distance

                        elif grid[_x][_y] == 0:
                            queue.append((_x, _y))
                            grid[_x][_y] = -1

            distance += 1
