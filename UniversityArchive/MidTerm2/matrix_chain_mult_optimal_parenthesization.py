matrices_dimensions = [(30, 30), (30, 35), (35, 35), (35, 10), (10, 15), (15, 30), (30, 30)]

# what are sizes of matrices from matrices_dimensions
matrices_sizes = [30, 35, 35, 10, 15, 30, 30]


# given the array of matrix dimensions, find the optimal parenthesize
# of the matrix chain multiplication
def matrix_chain_mult_optimal_parenthesization(matrices_sizes):
    # number of matrices
    n = len(matrices_dimensions)
    # initialize the cost matrix
    cost = [[0 for i in range(n)] for j in range(n)]
    # initialize the order matrix
    order = [[0 for i in range(n)] for j in range(n)]
    # find the optimal cost and order for every sub-chain of matrices
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            cost[i][j] = float("inf")
            for k in range(i, j):
                # cost of the current parenthesize
                current_cost = cost[i][k] + cost[k + 1][j] + matrices_sizes[i - 1] * matrices_sizes[k] * matrices_sizes[j]
                if current_cost < cost[i][j]:
                    cost[i][j] = current_cost
                    order[i][j] = k
    return cost, order


# print the optimal parenthesize
def print_optimal_parenthesize(order, i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        print_optimal_parenthesize(order, i, order[i][j])
        print_optimal_parenthesize(order, order[i][j] + 1, j)
        print(")", end="")


if __name__ == "__main__":
    cost, order = matrix_chain_mult_optimal_parenthesization(matrices_sizes)
    print("Cost matrix:")
    for i in range(1, len(cost)):
        print(cost[i][1:])
    print("Order matrix:")
    for i in range(1, len(order)):
        print(order[i][1:])
    print("Optimal parenthesize:")
    print_optimal_parenthesize(order, 1, len(matrices_sizes) - 1)
    # convert the cost matrix into Latex format


# Output:
# Cost matrix:
# [15750, 7875, 9375, 11875, 15125, 15125]
# [7875, 26250, 4375, 4375, 4375]
# [9375, 4375, 43750, 4375]
# [11875, 4375, 4375]
# [15125, 4375]
# [15125]
# Order matrix:
