# Youtube video for explenation: https://www.youtube.com/watch?v=L9Y1pqtptPE&ab_channel=BadriAdhikari
# https://sites.radford.edu/~nokie/classes/360/dp-rod-cutting.html

# Problem 1: Rod Cutting Given a price table for rods Determine the optimal revenue by inspection,
# with the corresponding optimal decompositions. Double-check your answer by writing and running the dynamic
# programming algorithm with recursive top-down implementation.

P = (3, 5, 7, 9, 12, 13, 16, 21, 23, 24, 28, 32)  # Price Table


# Top Down Recursive Approach
def cut_rod(length: int) -> int:
    """
    Find the optimal revenue for rod
    :param length: size of rod
    :return: optimal revenue
    """

    # Set initially a negative value, so it will always be less than the first option from the price table
    # Assuming that no cut has a negative price
    revenue = -1
    # find optimal revenue for every size before n
    # Cut the rod at every size from 1 to including itself (meaning no cut)
    for i in range(1, length + 1):
        # Cutting rod at i will give us two rods of size i & total length - i
        # |..i..|..length - i..|
        # Get revenue for cutting at i [ index = i-1 as i starts from 1]
        cutting_revenue = P[i - 1]
        # Calculate the optimal revenue for the leftover (length - i) part recursively
        leftover_revenue = cut_rod(length - i)
        # Add them together
        revenue_for_cutting_at_i = cutting_revenue + leftover_revenue
        # Chose maximum revenue between previous optimal and current cutting value
        # Previous cut value is stored in variable `revenue`
        revenue = max(revenue, revenue_for_cutting_at_i)
        # If cutting at i is more optimal than the previous optimal value revenue will be over-written by it
    return revenue


def cut_rod_with_memoization(length):
    # Set initially a negative values, so we can check if size at that index has been processed
    r = [-1] * (length + 1)
    return rod_cutting_memoized_helper(length, r)


def rod_cutting_memoized_helper(length, r):
    # rod size 0 costs nothing
    if length == 0:
        return 0
    # if rod size is already processed its index should have non-negative
    if r[length] >= 0:
        return r[length]
    # else for un-calculated rod size, find the optimal revenue
    else:
        # Set initially a negative value, so it will always be less than the first option from the price table
        revenue = -1
        # find optimal revenue for every size before n
        # Cut the rod at every size from 1 to including itself (meaning no cut)
        for i in range(1, length + 1):
            # Cutting rod at i will give us two rods of size i & total length - i
            # |..i..|..length - i..|
            # Get revenue for cutting at i [ index = i-1 as i starts from 1]
            cutting_revenue = P[i - 1]
            # Calculate the optimal revenue for the leftover (length - i) part recursively
            leftover_revenue = rod_cutting_memoized_helper(length - i, r)
            # Add them together
            revenue_for_cutting_at_i = cutting_revenue + leftover_revenue
            # Chose maximum revenue between previous optimal and current cutting value
            # Previous cut value is stored in variable `revenue`
            revenue = max(revenue, revenue_for_cutting_at_i)
            # If cutting at i is more optimal than the previous optimal value revenue will be over-written by it
        # update the revenues list with current optimal revenue
        r[length] = revenue

    return revenue


if __name__ == "__main__":
    for i, p in enumerate(P, 1):
        print(f"r{i} = {cut_rod_with_memoization(i)}")


# Bottom Up Approach
def bottom_up_cut_rod(rod_size):
    # list of optimal revenues for index size
    r = [-1] * (rod_size + 1)
    # rod of 0 size doesn't cost anything
    r[0] = 0
    # calculate revenue for every j size until the original size
    for j in range(1, rod_size + 1):
        # Set initially a negative value, so it will always be less than the first option from the price table
        revenue = -1
        # Cut the rod at every size from 1 to including itself (meaning no cut)
        for i in range(1, j + 1):
            # add revenue of i size rod with the previous optimal revenue for leftover j-i size rod
            # j - i < i - meaning there will always be right r[j-i] element in r list
            # note: P indexes start from 0 so P[i] = i - 1
            revenue = max(revenue, P[i - 1] + r[j - i])
        # update the revenues list with current optimal revenue
        r[j] = revenue

    # return revenues from optimal revenues list for rod_size

    return r[rod_size]


if __name__ == "__main__":
    for i, p in enumerate(P, 1):
        print(f"r{i} = {bottom_up_cut_rod(i)}")

c = 1  # fixed price for cutting rod


# rod cutting with memoization and bottom up approach
# calculate optimal revenue and number of cuts for each size
# get total price for cutting rod by multiplying number of cuts with fixed price
# subtract price for cutting rod from optimal revenue and return it
def rod_cutting_memoized_helper_and_cut_number(length, r, s):
    # rod size 0 costs nothing
    if length == 0:
        return 0, 0
    # if rod size is already processed its index should have non-negative
    if r[length] >= 0:
        return r[length], s[length]
    # else for un-calculated rod size, find the optimal revenue
    else:
        # Set initially a negative value, so it will always be less than the first option from the price table
        revenue = -1
        # find optimal revenue for every size before n
        # Cut the rod at every size from 1 to including itself (meaning no cut)
        for i in range(1, length + 1):
            # Cutting rod at i will give us two rods of size i & total length - i
            # |..i..|..length - i..|
            # Get revenue for cutting at i [ index = i-1 as i starts from 1]
            cutting_revenue = P[i - 1]
            # Calculate the optimal revenue for the leftover (length - i) part recursively
            # and number of times the cut is made
            leftover_revenue, leftover_cuts = rod_cutting_memoized_helper_and_cut_number(length - i, r, s)
            price_for_cuts = leftover_cuts * c
            # total revenue
            revenue_for_cutting_at_i = cutting_revenue + leftover_revenue - price_for_cuts
            # Chose maximum revenue between previous optimal and current cutting value
            # Previous cut value is stored in variable `revenue`
            # If cutting at i is more optimal than the previous optimal value revenue will be over-written by it
            if revenue < revenue_for_cutting_at_i:
                revenue = revenue_for_cutting_at_i
                # update the number of cuts for current optimal revenue
                s[length] = leftover_cuts + 1
        # update the revenues list with current optimal revenue
        r[length] = revenue
    return revenue, s[length]


def cut_rod_with_memoization_and_cut_number(length):
    # Set initially a negative values, so we can check if size at that index has been processed
    r = [-1] * (length + 1)
    # list of number of cuts for each size
    s = [0] * (length + 1)
    return rod_cutting_memoized_helper_and_cut_number(length, r, s)


if __name__ == "__main__":
    for i, p in enumerate(P, 1):
        r, s = cut_rod_with_memoization_and_cut_number(i)
        print(f"r{i} = {r}")
        print(f"s{i} = {s}")

