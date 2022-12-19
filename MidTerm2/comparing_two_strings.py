# Given two strings  X  and  Y .
# Determine the smallest set of  Z  of deletion and insertion of the characters to get string  Y  from the string  X .
#
# To solve this problem, use the Longest Common Subsequence  Z :
# If a character is absent in the longest common subsequence  Z , but present in the input  X , it must have been
# deleted (indicated by the "-").
# If a character is present in the input  Y , but absent in the longest common subsequence  Z , it must have been
# inserted (indicated by the "+").
#
# Example:
# Input:  X="kitten", Y="sitting"
# Output: "-k +s i t t -e +i n +g"

def validate_inputs(X, Y):
    if not isinstance(X, str):
        raise TypeError("X must be a string")
    if not isinstance(Y, str):
        raise TypeError("Y must be a string")


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


def format_string(X, Y, Z) -> str:
    """
    Formats the string to show what characters were deleted and inserted

    If a character is absent in the longest common subsequence  Z , but present in the input  X , it must have been deleted (indicated by the "-").
    If a character is present in the input  Y , but absent in the longest common subsequence  Z , it must have been inserted (indicated by the "+").

    :param X:
    :param Y:
    :param Z:
    :return: formatted Z string
    """
    x_index = 0
    z_index = 0
    y_index = 0
    formatted_string = ""

    while x_index < len(X) and y_index < len(Y):
        if X[x_index] != Z[z_index]:
            formatted_string += "-" + X[x_index]
            x_index += 1
        elif Y[y_index] != Z[z_index]:
            formatted_string += "+" + Y[y_index]
            y_index += 1
        else:
            formatted_string += Z[z_index]
            x_index += 1
            y_index += 1
            z_index += 1

    while x_index < len(X):
        formatted_string += "-" + X[x_index]
        x_index += 1

    while y_index < len(Y):
        formatted_string += "+" + Y[y_index]
        y_index += 1

    return formatted_string


if __name__ == "__main__":
    X = "kitten"
    Y = "sitting"
    Z = lcs(X, Y)

    # print the longest common subsequence
    print("Longest Common Subsequence: ", Z)

    print(format_string(X, Y, Z))
