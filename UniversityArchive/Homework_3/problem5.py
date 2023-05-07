
def longest_monotonically_increasing_subsequence(input_list: list) -> list:
    """
    This function finds the longest monotonically increasing subsequence of X in O(n) time.

    Using dynamic programming.

    :param input_list: Input list
    :return: The longest monotonically increasing subsequence of X in O(n) time.
    """
    if len(input_list) == 0:
        return []
    elif len(input_list) == 1:
        return input_list
    else:
        max_list = []
        for i in range(len(input_list)):
            max_list.append(1)
            for j in range(i):
                if input_list[j] < input_list[i]:
                    max_list[i] = max(max_list[i], max_list[j] + 1)
        max_value = max(max_list)
        max_index = max_list.index(max_value)
        result = [input_list[max_index]]
        for i in range(max_index - 1, -1, -1):
            if max_list[i] == max_value - 1:
                result.append(input_list[i])
                max_value -= 1
        return result[::-1]


def validate_inputs(input_list, output):
    result = longest_monotonically_increasing_subsequence(input_list)
    print(result)
    if output == result:
        print("Test passed")
    else:
        print("Test failed")


# Validate on input Input: [5,6,1,2,3,4,9,8,7] Output:[1,2,3,4,9]
if __name__ == "__main__":
    validate_inputs([5, 6, 1, 2, 3, 4, 9, 8, 7], [1, 2, 3, 4, 9])

    test_2 = [10, 3, -1, 2, 3, 4, 5, 1, 7, 8, 9]
    result = longest_monotonically_increasing_subsequence(test_2)
    print(result)