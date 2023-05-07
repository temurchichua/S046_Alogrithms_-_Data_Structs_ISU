# Problem 3: A Task-Scheduling Problem
# FFind a schedule for S that minimizes the total penalty incurred for missed deadlines.
# Notes: every task takes the single unit of time.

# STEP 1 : Sort the tasks into the early first form by deadlines
def sort_tasks(tasks: list, di: list, pi: list) -> None:
    """
    Inplace sort the tasks by deadlines
    :param tasks: list of task names
    :param di: list of deadline times
    :param pi: list of penalties
    :return: None
    """
    if len(tasks) != len(di) != len(pi):
        raise ValueError("The length of tasks, deadline and penalties must be the same")

    # sort using bubble sort
    for i in range(len(di)):
        for j in range(i + 1, len(di)):
            if di[i] > di[j]:
                di[i], di[j] = di[j], di[i]
                tasks[i], tasks[j] = tasks[j], tasks[i]
                pi[i], pi[j] = pi[j], pi[i]


# STEP 2: Iterate over the tasks to populate solution array
def minimize_total_penalty(tasks, di, pi):
    """
    Find a schedule for  S  that minimizes the total penalty incurred for missed deadlines.

    :param tasks:
    :param di:
    :param pi:
    :return:
    """
    time = 1
    solution = [tasks[0]]
    total_penalty = 0
    selected = 1
    for i in range(1, len(tasks)):
        if time + 1 <= di[i]:
            time += 1
            solution.append(tasks[i])
            selected += 1
        else:
            total_penalty += pi[i]

    return solution


def print_the_table(tasks, di, pi):
    """
    print horizontal table of tasks, deadlines and penalties

    The first line represents tasks, the second line represents deadlines and the third line represents penalties

    :param tasks:
    :param di:
    :param pi:
    :return:
    """

    print("Tasks\t\t", end="")
    for i in range(len(tasks)):
        print(f"{tasks[i]}\t", end="")

    t = 0
    print("\nTime\t\t", end="")
    for i in range(len(di)):
        t += 1
        print(f"{t}\t", end="")

    print("\nDeadlines\t", end="")
    for i in range(len(di)):
        print(f"{di[i]}\t", end="")

    print("\nPenalties\t", end="")
    for i in range(len(pi)):
        print(f"{pi[i]}\t", end="")

    print("\n")


def generate_table_from_tasks(result, tasks, di, pi):
    """
    Generate the table from the tasks, deadlines and penalties

    :param tasks:
    :param di:
    :param pi:
    :return:
    """
    res_di = []
    res_pi = []

    for task in result:
        # find index of the task
        index = tasks.index(task)

        res_di.append(di[index])
        res_pi.append(pi[index])

    return res_di, res_pi


if __name__ == "__main__":
    # Given a set  tasks={a,b,...,k}  which has deadlines and associated penalties
    tasks = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    # given di and pi as deadline and penalty of tasks

    di = [4, 3, 1, 4, 3, 1, 4, 6, 8, 2, 7]
    pi = [40, 50, 20, 30, 50, 30, 40, 10, 60, 20, 50]
    print("Initial table")
    print_the_table(tasks, di, pi)

    print("Sorted table")
    sort_tasks(tasks, di, pi)
    print_the_table(tasks, di, pi)

    optimal_tasks = minimize_total_penalty(tasks, di, pi)
    res_di, res_pi = generate_table_from_tasks(optimal_tasks, tasks, di, pi)

    print("Solution")
    print_the_table(optimal_tasks, res_di, res_pi)




