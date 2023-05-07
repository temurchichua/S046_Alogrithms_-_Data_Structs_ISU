# Problem 5: Longest Monotonically Increasing Subsequence
# Given a sequence X of n integer numbers.
#
# Usind Dynamic Programming, write a Python code that finds the longest monotonically increasing subsequence of X in
# O(n) time.
#
# Validate the inputs and test the code using the following inputs:
#
# Input: [5,6,1,2,3,4,9,8,7]
# Output:[1,2,3,4,9]

def longest_monotonically_increasing_subsequence(input_list: list) -> list:
    """
    This function finds the longest monotonically increasing subsequence of X in O(n) time.

    Using dynamic programming.

    :param input_list: Input list
    :return: The longest monotonically increasing subsequence of X in O(n) time.
    """
    if type(input_list) != list:
        raise ValueError("Input list of integers")
    # if the input list is empty, return empty list
    if len(input_list) == 0:
        return []
    # if the input list has only one element, return the element
    elif len(input_list) == 1:
        return input_list
    # if the input list has more than one element
    else:
        # initialize the longest subsequence list
        max_list = []
        # iterate over the input list
        for i in range(len(input_list)):
            # VALIDATE data type
            if type(i) != int and type(i) != float:
                raise ValueError("List should only contain numbers")
            # initialize the current subsequence list with 1 element
            max_list.append(1)
            # iterate until the current element
            for j in range(i):
                # if the current element is greater than the previous element
                if input_list[j] < input_list[i]:
                    # store the maximum value of the current subsequence list and the previous subsequence list
                    max_list[i] = max(max_list[i], max_list[j] + 1)
        # find the maximum value in the longest subsequence list
        max_value = max(max_list)
        # find the index of the first occurrence of maximum value in the longest subsequence list
        max_index = max_list.index(max_value)
        # slice the input list from the index of the first occurrence of maximum value in the longest subsequence list
        # to the span of the maximum value
        result = input_list[max_index - max_value + 1: max_index + 1]

        return result


def validate_inputs(test_input, expected_output):
    if expected_output == longest_monotonically_increasing_subsequence(test_input):
        print("Test passed")
    else:
        print("Test failed")


# Validate on input Input: [5,6,1,2,3,4,9,8,7] Output:[1,2,3,4,9]
validate_inputs(test_input=[5, 6, 1, 2, 3, 4, 9, 8, 7],
                expected_output=[1, 2, 3, 4, 9])

# Validate on input Input: [5,6,1,2,3,4,9,8,7] Output:[1,2,3,4,9]
if __name__ == "__main__":
    validate_inputs([5, 6, 1, 2, 3, 4, 9, 8, 7], [1, 2, 3, 4, 9])
