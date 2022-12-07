# Problem 4: Longest Palindrome Subsequence
# A palindrome is a nonempty string over some alphabet that reads the same forward and backward.
#
# For example "აი ია" is a palindrome (Assuming that space is also belongs to the alphabet).
#
# Using dynamic pgoramming, write a Python code that finds the longest palindrome that is a subsequence of a given
# input string.
#
# Validate the inputs and test the code using the following inputs:
#
# Input: "ABBDCACB"
# Output: "BCACB"

def longest_palindrome_subsequence(input_string: str) -> str:
    """
    This function finds the longest palindrome that is a subsequence of a given input string.

    :param input_string: Input string
    :return: The longest palindrome that is a subsequence of a given input string.
    """
    if len(input_string) == 0:
        return ""
    elif len(input_string) == 1:
        return input_string
    elif input_string[0] == input_string[-1]:
        return input_string[0] + longest_palindrome_subsequence(input_string[1:-1]) + input_string[-1]
    else:
        str1 = longest_palindrome_subsequence(input_string[1:])
        str2 = longest_palindrome_subsequence(input_string[:-1])
        return str1 if len(str1) > len(str2) else str2


def validate_inputs(input_string, output):
    if output == longest_palindrome_subsequence(input_string):
        print("Test passed")
    else:
        print("Test failed")


# Validate on input Input: ABBDCACB Output: BCACB
if __name__ == "__main__":
    validate_inputs("ABBDCACB", "BCACB")
