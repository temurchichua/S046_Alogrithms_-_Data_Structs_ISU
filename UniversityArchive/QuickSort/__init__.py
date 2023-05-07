import random

TEST = 0
def quick_sort(array):
    size = len(array)
    if size < 2:
        return array
    # pivot_index = random.randint(0, size - 1)
    pivot_index = size // 2
    pivot = array[pivot_index]
    array[-1], array[pivot_index] = array[pivot_index], array[-1]

    i = 0
    for j in range(size - 1):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            print(f"Swapped for pivot {pivot} array {array} {array[i]} ({i}) <> {array[j]} ({j})")
            i += 1

    array[i], array[-1] = array[-1], array[i]
    # print(f"Sorted for pivot {pivot} array {array}")
    less_then_pivot = quick_sort(array[:i])
    greater_then_pivot = quick_sort(array[i + 1:])
    return less_then_pivot + [array[i]] + greater_then_pivot


A = [8, 4, 5, 13, 11, 14, 7, 3, 10, 2, 9, 6, 15, 12, 1]
sA = quick_sort(A)
print(sA)

if TEST:
    for _ in range(100):
        A = random.sample(range(0, 100), 10)
        sA = quick_sort(A)
        assert sA == sorted(A, reverse=False)
