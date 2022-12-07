# Problem 3: Fibonacci Numbers
# The Fibonacci numbers are defined by recurrence:
#
# F0=0,
# F1=1,
# Fn=Fn−1+Fn−2  for all  n≥2 .
# Using dynamic programming, write a Python code that computes the  n -th Fibonacci number in  O(n) -time.
#
# Validate the inputs and test the code using the following inputs:
# Input: 0,1,10
# Output: 55


def fib(f0, f1, n) -> int:
    """
    This function computes the n-th Fibonacci number in O(n) -time.

    :param f0: F0
    :param f1: F1
    :param n: n
    :return: n-th Fibonacci number
    """
    if n == 0:
        return f0
    elif n == 1:
        return f1
    else:
        return fib(n - 1) + fib(n - 2)


def validate_inputs(f0, f1, n, output):
    if output == fib(f0, f1, n):
        print("Test passed")
    else:
        print("Test failed")


# Validate on input Input: 0,1,10 Output: 55
validate_inputs(0, 1, 10, 55)
