import random


class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def valid_index(self, index, raise_exception=False):
        if index > self.size - 1:
            if raise_exception is True:
                raise IndexError(f"Index {index} is out of range")
            else:
                return False
        else:
            return True

    def get_left_child_index(self, i):
        if self.valid_index(i):
            index = 2 * i + 1
            return index

    def get_right_child_index(self, i):
        if self.valid_index(i):
            index = 2 * i + 2
            return index

    def get_parent_index(self, i):
        if self.valid_index(i):
            return (i - 1) // 2

    def get_left_child(self, i):
        index = self.get_left_child_index(i)
        if not self.valid_index(index, raise_exception=False):
            raise IndexError(f"Index {i} has no left child")

    def get_right_child(self, i):
        index = self.get_right_child_index(i)
        if not self.valid_index(index, raise_exception=False):
            raise IndexError(f"Index {i} has no right child")

    def parent(self, i):
        index = self.get_paren_index(i)
        if not self.valid_index(index, raise_exception=False):
            raise IndexError(f"Node at {i} has no parent")

    def peek(self):
        if self.size == 0:
            raise ValueError("Heap is empty")
        else:
            return self.heap[0]

    def swap(self, i, j):
        try:
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        except IndexError:
            raise IndexError(f"Index {i} or {j} is out of range")

    def heapify_up(self):
        if self.size == 0:
            return

        current_index = self.size - 1
        parent_index = self.get_parent_index(current_index)

        while current_index != 0 and self.valid_index(parent_index):
            if self.heap[current_index] > self.heap[parent_index]:
                return
            else:
                self.swap(current_index, parent_index)

            current_index = parent_index
            parent_index = self.get_parent_index(current_index)

    def heapify_down(self):
        if self.size == 0:
            return

        current_index = 0
        child_index = self.get_left_child_index(current_index)

        while self.valid_index(child_index):
            if self.valid_index(self.get_right_child_index(current_index)):
                if self.heap[self.get_right_child_index(current_index)] < self.heap[child_index]:
                    child_index = self.get_right_child_index(current_index)

            if self.heap[current_index] < self.heap[child_index]:
                return
            else:
                self.swap(current_index, child_index)

            current_index = child_index
            child_index = self.get_left_child_index(current_index)

    def insert(self, item):
        """
        O log n
        """
        self.heap.append(item)
        self.size += 1
        self.heapify_up()

    def remove(self):
        self.swap(0, self.size)
        self.heap.pop()

    def replace_head(self, value):
        if self.heap:
            self.heap[0] = value
        else:
            raise IndexError("Can't replace value at index 0 in empty heap. Insert the value first.")

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.heap)

    def __repr__(self):
        return self.heap


# items = [random.randint(0, 10) for _ in range(10)]
items = [9, 4, 7, 1, -2, 6, 5]
if __name__ == "__main__":
    print(items)
    heap = Heap()
    for item in items:
        print(f"{item} -> {heap}")
        heap.insert(item)
        print(heap)
