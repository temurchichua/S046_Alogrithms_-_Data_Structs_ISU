import sympy as sp

# Define the variables
n = sp.Symbol('n')

x = 0

n_sqr_100 = 100 * n ** 2
n_sqr = n ** 2

if __name__ == "__main__":
    while 100 * n ** 2 > 2 ** n:
        n += 1

    print(f"n = {n}")
