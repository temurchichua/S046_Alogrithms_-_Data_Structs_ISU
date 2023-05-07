import bisect

obstacles = [3, 1, 5, 6, 4, 2]
expected = [1, 1, 2, 3, 2, 2]


def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
    size = len(obstacles)
    cache = [1] * size
    lis = []

    for i, height in enumerate(obstacles):
        index = bisect.bisect_right(lis, height)

        if index == len(lis):
            lis.append(height)
        else:
            # updated height at that index in answer
            lis[index] = height

        cache[i] = index + 1

    return cache


if __name__ == '__main__':
    result = longestObstacleCourseAtEachPosition(longestObstacleCourseAtEachPosition, obstacles)
    print(f"result: {result}")
    print(f"expected: {expected}")
    assert result == expected
