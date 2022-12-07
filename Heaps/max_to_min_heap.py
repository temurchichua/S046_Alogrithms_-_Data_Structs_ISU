# Given an array of integers, representing a Max-Heap, in-place convert the array into the Min-Heap in linear time.


def max_to_min_heap(heap: list[int]) -> None:
    """
    In-place convert a Max-Heap into a Min-Heap.
    """
    #  Convert the Max-Heap into a Min-Heap.
    for i in range(len(heap) // 2, -1, -1):
        min_heapify(heap, i)


def min_heapify(heap: list[int], index: int) -> None:
    """
    Convert a subtree into a Min-Heap.
    """
    #  Check the left child.
    left_child_index = 2 * index + 1
    if left_child_index < len(heap):
        if heap[left_child_index] < heap[index]:
            heap[index], heap[left_child_index] = heap[left_child_index], heap[index]
        # Check the left child's children.
        min_heapify(heap, left_child_index)

    #  Check the right child.
    right_child_index = 2 * index + 2
    if right_child_index < len(heap):
        if heap[right_child_index] < heap[index]:
            heap[index], heap[right_child_index] = heap[right_child_index], heap[index]
        # Check the right child's children.
        min_heapify(heap, right_child_index)


if __name__ == "__main__":
    heap = [9, 4, 7, 1, -2, 6, 5]
    max_to_min_heap(heap)
    print(heap)
