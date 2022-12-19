# Problem 1: An Activity-Selection Problem
# Given a set  S={a1,a2,...,a11}  of  11  proposed activities that wish to use a resource, such as a lecture hall:
# Find a maximum-size subset of mutually compatible activities.

# STEP 1 : Sort the activities according to their finish time
def sort_activities(si: list, fi: list) -> None:
    """
    Inplace sort the activities by their finish time
    :param si: list of start times
    :param fi: list of finish times
    :return: None
    """

    if len(si) != len(fi):
        raise ValueError("The length of start time and finish time must be the same")

    # sort using bubble sort
    for i in range(len(fi)):
        for j in range(i + 1, len(fi)):
            if fi[i] > fi[j]:
                fi[i], fi[j] = fi[j], fi[i]
                si[i], si[j] = si[j], si[i]


# STEP 2 : Initiate solution array
sol = []


# STEP 3: Iterate over the activities to populate solution array
def check_activity_matching(si, fi, sol):
    sol.append(0)
    for i in range(1, len(si)):
        # if current time is great or equal to the finish time of the previous activity
        if si[i] >= fi[sol[-1]]:
            sol.append(i)


# STEP 4: Print the solution
def turn_sol_into_answer(sol, si, fi):
    return [(si[i], fi[i]) for i in sol]


if __name__ == "__main__":
    # given si and fi as start and finish time of activity ai
    si = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    fi = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

    sort_activities(si, fi)
    check_activity_matching(si, fi, sol)
    print(turn_sol_into_answer(sol, si, fi))
