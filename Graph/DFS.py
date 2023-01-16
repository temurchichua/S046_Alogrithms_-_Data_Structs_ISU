n: int = 5  # number of nodes in graph
g = list()  # adjacency list representing graph
visited = [False] * n  # list of boolean values representing if node at index has been visited

start_node = 0


def dfs(at):
    if visited[at]:
        return

    visited[at] = True

