# Given a list of strings where no string is a substring of another string, find the shortest string that contains all the strings in the list.
from comparing_two_strings import lcs

list_of_strings = ["CATGC", "CTAAGT", "GCTA", "TTCA", "ATGCATC"]
expected_output = "GCTAAGTTCATGCATC"


def find_shortest_superstring(los: list) -> str:
    """
    Find the shortest string that contains all the strings in the list
    :param los: list of strings
    :return: shortest string that contains all the strings in the list
    """
    # check if the input is valid
    if not validate_input(los):
        return "Invalid input"

    # find the shortest string that contains all the strings in the list
    while len(los) > 1:
        print(los)
        # reset the overlap
        max_lcs_length = 0
        # reset the indices of the two strings
        max_lcs_indices = [0, 0]
        # find the two strings that has the biggest overlap
        for i in range(len(los)):
            for j in range(i + 1, len(los)):
                # find the longest common substring
                lcs_length = len(lcs(los[i], los[j]))
                # check if the current overlap is bigger than the previous overlap
                if lcs_length > max_lcs_length:
                    # update the overlap
                    max_lcs_length = lcs_length
                    # update the indices of the two strings
                    max_lcs_indices = [i, j]

        # merge the two strings
        A = los[max_lcs_indices[0]]
        B = los[max_lcs_indices[1]]
        print(f"Inital strings are {A} and {B}")

        # find the shortest string that contains both A and B strings
        # reset the flag
        added = False
        for i in range(1, len(A)+1):  # O(n)
            if A[i:] == B[:len(A) - i]:
                print(f"compared strings are {A[i:]} and {B[:len(A) - i]}")
                A = A[:i] + B
                added = True
                break
            elif B[i:] == A[:len(B) - i]:
                print(f"compared strings are {B[i:]} and {A[:len(B) - i]}")
                A = B[:i] + A
                added = True
                break

        # if the current string has not been added to the shortest string, add the current string to the shortest string
        if not added:
            A += B

        print(f"Shortest string is {A}")
        # remove the two strings from the list
        los.remove(los[max_lcs_indices[0]])
        los.remove(los[max_lcs_indices[1] - 1])
        # add the shortest string to the list
        los.append(A)
    # return the shortest string
    return los[0]


def validate_input(los: list) -> bool:
    """
    Validate the input
    :param los: list of strings
    :return: True if the input is valid, False otherwise
    """
    # check if the type of input is valid
    if not isinstance(los, list):
        return False
    # check if the list of strings is empty
    if not los:
        return False
    # check if the list of strings contains only strings
    for char in los:
        if not isinstance(char, str):
            return False
    # check if the list of strings contains only unique strings
    if len(los) != len(set(los)):
        return False
    # check if any string is a substring of another
    for i in range(len(los)):
        for j in range(i + 1, len(los)):
            if los[i] in los[j] or los[j] in los[i]:
                return False
    return True


if __name__ == "__main__":
    # find the shortest superstring
    shortest_superstring = find_shortest_superstring(list_of_strings)
    # check if the output is correct
    if shortest_superstring == expected_output:
        print(shortest_superstring)
    else:
        print(f"My Solution Bad: {shortest_superstring}")
        print(f"Expected Output: {expected_output}")

# CATGCATC
# GCTAAGTTCATGCATC
list_of_strings = ["CATGC", "CTAAGT", "GCTA", "TTCA", "ATGCATC"]
