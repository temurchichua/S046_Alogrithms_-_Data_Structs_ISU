nums = [10, 9, 2, 5, 3, 7, 101, 18]
expected = 4


def lengthOfLIS(nums: list[int]) -> int:
    size = len(nums)

    LIS = [1] * size

    for i in range(size, -1, -1):
        for j in range(i + 1, size):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

    return max(LIS)


if __name__ == '__main__':
    print(lengthOfLIS(nums))
    print("Expected: {}".format(expected))

    assert lengthOfLIS(nums) == expected
