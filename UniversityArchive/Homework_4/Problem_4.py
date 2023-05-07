# Problem 4: Fitting Shelves Problem
# Given the length of a wall  w  and infinite shelves of two lengths  s  (small) and  l  (large).
#
# Large shelves are cheaper than the smaller ones.
#
# Write Python code that finds the best solution for placing the shelves in the wall in a way that leaves as little
# empty space as possible.
#
# Preference is given to the optimal solution with more long shelves since a longer shelf is cheaper, but the cost is
# secondary, first priority is to minimize empty space on the wall.
#
# Note: You need to use Greedy approach to solve this problem!

def minimize_empty_space(w: int, s: int, l: int):
    """
    Fill the shell space w as much as possible with small s and large l sized shelves

    :param w: size of the wall
    :param s: size of the small shelf
    :param l: size of the large shelf
    :return: list of shelves
    """
    number_of_l = 0
    number_of_s = 0
    leftover = w
    best_solution = [number_of_s, number_of_l, leftover]
    # fill the wall with large shelves
    while w >= l:
        number_of_l += 1
        w -= l
        leftover = w
        while leftover >= s:
            number_of_s += 1
            leftover -= s

        if leftover < best_solution[2]:
            best_solution = [number_of_s, number_of_l, leftover]
        number_of_s = 0
    return best_solution


if __name__ == "__main__":
    # Input:
    w, s, l = 24, 3, 5
    n_s, n_l, empty_space = minimize_empty_space(w, s, l)
    print(f"S = {n_s}, L = {n_l}, Empty Space = {empty_space}")


