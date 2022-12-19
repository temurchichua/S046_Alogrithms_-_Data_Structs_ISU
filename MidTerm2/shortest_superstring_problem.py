# Given a list of strings where no string is a substring of another string, find the shortest string that contains all the strings in the list.
list_of_strings = ["CATGC", "CTAAGT", "GCTA", "TTCA", "ATGCATC"]
expected_output = "GCTAAGTTCATGCATC"

def lcs(X, Y) -> str:
    """
    Returns the string of the longest common subsequence of two strings

    :param X:
    :param Y:
    :return: formatted string of lcs
    """
    # length of the strings
    m = len(X)
    n = len(Y)
    Z = ""
    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
    """
    for i in range(m + 1):
        for j in range(n + 1):
            # if the first string is empty, then the length of the longest common subsequence is 0
            if i == 0 or j == 0:
                L[i][j] = 0

            elif X[i - 1] == Y[j - 1]:
                # if the characters are the same, then the length of the longest common subsequence is 1 + the length
                # of the longest common subsequence of the remaining characters
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                # if the characters are not the same, then the length of the longest common subsequence is the maximum
                # of the length of the longest common subsequence of the remaining characters of the first string
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Following code is used to print LCS
    index = L[m][n]
    # Create a character array to store the lcs string
    Z = [""] * (index + 1)
    Z[index] = ""

    # Start from the right-most-bottom-most corner and one by one store characters in Z
    i = m
    j = n
    while i > 0 and j > 0:
        # If current character in X[] and Y are same, then current character is part of LCS
        if X[i - 1] == Y[j - 1]:
            Z[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        # If not same, then find the larger of two and go in the direction of larger value
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(Z)


def find_shortest_string(strings):
    # sort the strings in ascending order of length
    # strings = sorted(strings, key=len)

    # initialize the shortest string with the longest common subsequence
    A = strings[0]

    for i in range(1, len(strings)):
        A = lcs(A, strings[i])
    print(A)

    # loop through the strings starting from the second string
    for B in strings:
        # initialize a flag to indicate if the current string has been added to the shortest string
        added = False
        print(f"Comparing {A} and {B}")
        # check if the current string is already a subset of the shortest string
        if B in A:
            # it's in the problem statement, but I'm just trying to greate the general solution
            continue

        # Find the longest common substring between the shortest string and the current string
        # loop through the shortest string
        for i in range(len(A)): # O(n)
            # loop through the current string
            for j in range(len(B)): # O(n)
                # check if the characters at the current indices are equal
                if A[i] == B[j]:
                    # check if the substring starting from the current indices is a substring of the current string
                    if A[i:] in B:
                        # add the substring to the shortest string
                        A = A[:i] + B
                        # set the flag to True
                        added = True
                        # break out of the loop
                        break   # O(1)
                    # check if the substring starting from the current indices is a substring of the shortest string
                    elif B[j:] in A:
                        # set the flag to True
                        added = True
                        # break out of the loop
                        break

        # if the current string has not been added to the shortest string, add the current string to the shortest string
        if not added:
            A += B

        print(f"Shortest string is {A}")

    return A


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
    shortest_superstring = find_shortest_string(list_of_strings)
    # check if the output is correct
    if shortest_superstring == expected_output:
        print(shortest_superstring)
    else:
        print(f"My Solution Bad: {shortest_superstring}")
        print(f"Expected Output: {expected_output}")

# CATGCATC
# GCTAAGTTCATGCATC