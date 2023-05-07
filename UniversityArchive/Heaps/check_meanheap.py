inputs = (
    [15, 10, 5, 4, 3, 2],
    [15, 3, 5, 4, 10, 2]
)


def is_max_heap(heap: list, index: int) -> bool:
    size = len(heap)
    if index >= size:
        return True

    #  Check the left child.
    left_child_index = 2 * index + 1
    if left_child_index < size:
        if heap[left_child_index] > heap[index]:
            return False
        # Check the left child's children.
        if not is_max_heap(heap, left_child_index):
            return False

    #  Check the right child.
    right_child_index = 2 * index + 2
    if right_child_index < size:
        if heap[right_child_index] > heap[index]:
            return False
        # Check the right child's children.
        if not is_max_heap(heap, right_child_index):
            return False

    return True


for input in inputs:
    if is_max_heap(input, 0):
        print("Given array is a Max-Heap.")
    else:
        print("Given array is not a Max-Heap.")
