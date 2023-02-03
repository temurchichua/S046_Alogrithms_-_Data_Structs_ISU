edges = [
    ["b", "c", 2],
    ["a", "c", 3],
    ["b", "d", 4],
    ["a", "b", 5],
]

visited = []


def mst(edges, start_node):
    if start_node in visited:
        return
    visited.append(start_node)
    neighbour_edges = []
    for edge in edges:
        if start_node in edge:
            neighbour_edges.append(edge)

    print(neighbour_edges)

    next_edge = neighbour_edges[0]
    for edge in neighbour_edges:
        if edge[2] < next_edge[2]:
            next_edge = edge

    current_node = next_edge[1]
    print(current_node)
    mst(edges, current_node)


if __name__ == "__main__":
    mst(edges, "a")
