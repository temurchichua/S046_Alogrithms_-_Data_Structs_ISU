# illustrate the operation of partition procedure
# You need to draw the array shown below for each step of partition procedure.
A = [8, 4, 5, 13, 11, 14, 7, 3, 10, 2, 9, 6, 15, 12, 1]


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for n, j in enumerate(range(p, r), 1):
        if A[j] <= x:
            i = i + 1
            exchange(A, i, j)
        print(f"{n}. {x} {A}  i = {i} j = {j}")
    exchange(A, i + 1, r)
    return i + 1


def exchange(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

if __name__ == "__main__":
    print(f"15. {partition(A, 0, len(A) - 1)} {A}")
