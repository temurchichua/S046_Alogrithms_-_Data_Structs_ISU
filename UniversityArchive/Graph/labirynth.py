from pprint import pprint

"""
You are in the middle of the labyrinth  m,n .

You can move only in four directions: Up, Right, Down, Left.


Hint. Represent Matrix as a Graph and then use BFS algorithm.
Write a Python code that check if there is a path out from the Labyrinth.
You escape the labyrinth if you reach one of the edges of the matrix.


Output: Print "There is a path out!" or "You will be here forever!".
"""

Labyrinth = [
    [0, 1, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 1, 0, 0]
]

# You are in the middle of the labyrinth  m,n .
middle = (len(Labyrinth) // 2, len(Labyrinth[0]) // 2)
# You can move only in four directions: Up, Right, Down, Left.
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def matrix_to_graph(labyrinth) -> dict:
    """
    Turn matrix into graph of possible moves in the labyrinth as adjacency list
    :param labyrinth: matrix of labyrinth
    :return: adjacency list
    """
    # Empty graph as dictionary
    # Validate input
    if not labyrinth or not isinstance(labyrinth, list):
        raise ValueError('Invalid input')
    graph = {}
    # Iterate over matrix rows
    for i in range(len(labyrinth)):
        # validate row
        if not isinstance(labyrinth[i], list):
            raise ValueError('Invalid input')
        # Iterate over matrix columns
        for j in range(len(labyrinth[0])):
            # validate cell
            if not isinstance(labyrinth[i][j], int):
                raise ValueError('Invalid input')
            # If an emtpy cell add into the adjacency list
            if labyrinth[i][j] == 0:
                graph[(i, j)] = []
                # get all the neighbours of the cell
                for direction in directions:
                    # get new coordinates
                    new_i = i + direction[0]
                    new_j = j + direction[1]
                    # check if the new coordinates are within the matrix
                    if 0 <= new_i < len(labyrinth) and 0 <= new_j < len(labyrinth[0]):
                        # if the new coordinates are empty cell add them to the adjacency list
                        if labyrinth[new_i][new_j] == 0:
                            graph[(i, j)].append((new_i, new_j))
    return graph


if __name__ == '__main__':
    adj_list = matrix_to_graph(Labyrinth)
    pprint(adj_list)
