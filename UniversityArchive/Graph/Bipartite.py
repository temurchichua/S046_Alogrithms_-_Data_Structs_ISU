"""
Problems C1: Bipartite Graph
An undirected graph is called a bipartite graph if its vertices may be colored in two colors in such a way that each edge connects vertices of different colors.

Write a Python code that checks whether a graph is a bipartite graph in  O(V+E)  time.

Test the code using the following inputs:

Input: The individual graph generated below.

Output: Print "Graph is bipartite" or "Graph is not bipartite".

Hint. After we choose the color of some vertex, the colors of all other vertices of the same component are uniquely determined.
"""
# Enter your student ID
ID = 20

import random

random.seed(ID)

import networkx as nx
import matplotlib.pyplot as plt
import pylab

G = nx.DiGraph();
V = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

for u in V:
    for v in V:
        if u != v:
            edge = random.randint(0, 4)
            if not edge:
                w = 1
                G.add_edges_from([(u, v)], weight=w)

edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])
plt.figure(1, figsize=(6, 6))
pos = nx.circular_layout(G)
nx.draw_networkx(G, pos, node_size=2000, arrowsize=20, font_size=20, arrows=False)
pylab.show()


def is_bipartite(G):
    """
    Check if the graph is bipartite
    :param G:
    :return:
    """
    # Validate input
    if not G or not isinstance(G, nx.DiGraph):
        raise ValueError('Invalid input')
    # Color the nodes with two colors using BFS
    # Get the first node
    node = list(G.nodes)[0]
    # Create a queue
    queue = [node]
    # Create a dictionary to store the colors
    colors = {node: 1}
    # Color the first node
    # Iterate until the queue is empty
    while queue:
        # Get the node from the queue
        node = queue.pop(0)
        # Get the neighbours of the node
        neighbours = list(G.neighbors(node))
        # Iterate over the neighbours
        for neighbour in neighbours:
            # If the neighbour is not colored
            if neighbour not in colors:
                # Color it with the other color
                colors[neighbour] = 1 - colors[node]
                # Add it to the queue
                queue.append(neighbour)
            # If the neighbour is colored with the same color
            elif colors[neighbour] == colors[node]:
                # Return False
                return False
    # Return True
    return True


def output_result(G):
    """
    Output the result
    :param G:
    :return:
    """
    # Output the result
    if is_bipartite(G):
        print('Graph is bipartite')
    else:
        print('Graph is not bipartite')


# Output the result
if __name__ == '__main__':
    print(is_bipartite(G))
