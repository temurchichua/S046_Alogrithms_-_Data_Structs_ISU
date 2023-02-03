"""
Given list of inputs and graph G=(V,E) ,
Write python code that for S in inputs checks if it is the smallest possible set that covers the given graph G=(V,E) .
"""

graph = {"A": ["B", "D"],
         "B": ["A", "C"],
         "C": ["B", "D", "E"],
         "D": ["A", "C", "E"],
         "E": ["D", "C"],
         }

inputs = [
    ["A", "B", "E"],
    ["A", "D", "C"],
    ["A", "B", "C"],
    ["A", "B", "C", "D"],
]


def covers_graph(graph, list_to_check):
    """
    Checks whether given set S covers the given graph
    """
    # Validate input
    if not graph or not isinstance(graph, dict) or not list_to_check or not isinstance(list_to_check, list):
        raise ValueError('Invalid input')

    # check if all edges are covered
    for v in graph:
        # if current vertex not in S
        if v not in list_to_check:
            # check if v has a neighbour in S
            for u in graph[v]:
                # if not v but u in S
                if u in list_to_check:
                    # break the loop and continue with the next vertex
                    break
            else:
                # if no neighbour of v in S
                return False
    return True


def is_vertex_cover(graph, list_to_check):
    """
    Checks whether given set  S  is the smallest possible set that covers the given graph
    Hint: You can assume, that set  S  is not smallest possible set, if you can remove some vertex  v  from  S  and set  (S−{v})  still covers graph  G .

    :param graph:
    """
    # Validate input
    if not graph or not isinstance(graph, dict) or not list_to_check or not isinstance(list_to_check, list):
        raise ValueError('Invalid input')

    for vertex in list_to_check:
        list_to_check.remove(vertex)
        if not covers_graph(graph, list_to_check):
            list_to_check.append(vertex)
            return False
        list_to_check.append(vertex)
    return True


def test_is_vertex_cover(inputs):
    for S in inputs:
        print("Input: ", S)
        if is_vertex_cover(graph, S):
            print("Output: The set of vertices S is a smallest possible set")
        else:
            print("Output: The set of verticies S is not the smallest possible set")


test_is_vertex_cover(inputs)
