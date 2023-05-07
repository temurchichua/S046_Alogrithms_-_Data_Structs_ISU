# Problem 1: Rod Cutting Given a price table for rods Determine the optimal revenue by inspection,
# with the corresponding optimal decompositions. Double-check your answer by writing and running the dynamic
# programming algorithm with recursive top-down implementation.

price_table = [2, 7, 10, 11, 12, 19, 20, 25, 28, 30]


def rod_cutting(price_table, rod_length):
    if rod_length == 0:
        return 0
    q = -1
    for i in range(rod_length):
        q = max(q, price_table[i] + rod_cutting(price_table, rod_length - i - 1))
    return q


def rod_cutting_memoized(price_table, rod_length):
    r = [-1] * (rod_length + 1)
    return rod_cutting_memoized_helper(price_table, rod_length, r)


def rod_cutting_memoized_helper(price_table, rod_length, r):
    if r[rod_length] >= 0:
        return r[rod_length]
    if rod_length == 0:
        q = 0
    else:
        q = -1
        for i in range(rod_length):
            q = max(q, price_table[i] + rod_cutting_memoized_helper(price_table, rod_length - i - 1, r))
    r[rod_length] = q
    return q


def rod_cutting_bottom_up(price_table, rod_length):
    r = [-1] * (rod_length + 1)
    r[0] = 0
    for j in range(1, rod_length + 1):
        q = -1
        for i in range(j):
            q = max(q, price_table[i] + r[j - i - 1])
        r[j] = q
    return r[rod_length]


def rod_cutting_bottom_up_with_solution(price_table, rod_length):
    r = [-1] * (rod_length + 1)
    s = [-1] * (rod_length + 1)
    r[0] = 0
    for j in range(1, rod_length + 1):
        q = -1
        for i in range(j):
            if q < price_table[i] + r[j - i - 1]:
                q = price_table[i] + r[j - i - 1]
                s[j] = i
        r[j] = q
    return r[rod_length], s


def print_rod_cutting_solution(price_table, rod_length):
    revenue, solution = rod_cutting_bottom_up_with_solution(price_table, rod_length)
    print(f"Revenue: {revenue}")
    while rod_length > 0:
        print(f"Cut: {solution[rod_length] + 1}")
        rod_length -= solution[rod_length] + 1


if __name__ == "__main__":
    print(rod_cutting(price_table, 10))
    print(rod_cutting_memoized(price_table, 10))
    print(rod_cutting_bottom_up(price_table, 10))
    print_rod_cutting_solution(price_table, 10)

# Problem 2: Cutting is Expensive Consider a modification of the rod-cutting problem in which, in addition to a price
# pi  for each rod, each cut incurs a fixed cost of  c . The revenue associated with a solution is now the sum of the
# prices of the pieces minus the costs of making the cuts. Write a Python code that solves this modified problem
# using the dynamic-programming.

price_table = [2, 7, 10, 11, 12, 19, 20, 25, 28, 30]
cost = 1


def rod_cutting_with_cost(price_table, rod_length, cost):
    r = [-1] * (rod_length + 1)
    r[0] = 0
    for j in range(1, rod_length + 1):
        q = -1
        for i in range(j):
            q = max(q, price_table[i] + r[j - i - 1] - cost)
        r[j] = q
    return r[rod_length]


def rod_cutting_with_cost_with_solution(price_table, rod_length, cost):
    r = [-1] * (rod_length + 1)
    s = [-1] * (rod_length + 1)
    r[0] = 0
    for j in range(1, rod_length + 1):
        q = -1
        for i in range(j):
            if q < price_table[i] + r[j - i - 1] - cost:
                q = price_table[i] + r[j - i - 1] - cost
                s[j] = i
        r[j] = q
    return r[rod_length], s


def print_rod_cutting_with_cost_solution(price_table, rod_length, cost):
    revenue, solution = rod_cutting_with_cost_with_solution(price_table, rod_length, cost)
    print(f"Revenue: {revenue}")
    while rod_length > 0:
        print(f"Cut: {solution[rod_length] + 1}")
        rod_length -= solution[rod_length] + 1

if __name__ == "__main__":
    print(rod_cutting_with_cost(price_table, 10, cost))
    print_rod_cutting_with_cost_solution(price_table, 10, cost)

