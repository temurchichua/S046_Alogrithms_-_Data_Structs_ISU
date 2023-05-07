# MIT License

# Copyright (c) 2018 Alexander L. Hayes

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
=====================================
Optimal Matrix Chain Ordering Problem
=====================================

Python implementation of the "Matrix-Chain-Order" algorithm from Thomas H.
Cormen et al. "Introduction to Algorithms Third Edition", which uses Dynamic
Programming to determine the optimal parenthesization for Matrix-chain
multiplication.

Overview
--------

.. topic:: Matrix Chain Multiplication

  "We state the *matrix-chain multiplication problem* as follows: given a chain
  ``A_1, A_2, ..., A_n`` of ``n`` matrices, where for ``i = 1, 2, ..., n``,
  matrix ``A_i`` has dimension ``p_(i-1) * p_i``, fully parenthesize the
  product ``A_1, A_2, ..., A_n`` in a way that minimizes the number of scalar
  multiplications."

Cormen et al. show the algorithm for this at the bottom of page 375, which
returns two tables. The "S" table may be further input to the
"Print-Optimal-Parens" algorithm at the bottom of page 377 to display the
optimal ordering.

Both algorithms are implemented here. They may be invoked from the commandline
to show (i,j) entries in the S matrix, and to display the optimal parentheses
for the multiplication.

Example Usage
-------------

.. code-block:: python

  $ python MatrixChainOrdering.py --chain 2,20,4,6
  ((A_1A_2)A_3)

  $ python MatrixChainOrdering.py --chain 2,20,4,6 --verbose
  (i,j) = (1,1): 0
  (i,j) = (2,2): 0
  (i,j) = (3,3): 0
  (i,j) = (1,2): 160
  (i,j) = (2,3): 480
  (i,j) = (1,3): 208
"""


def matrix_chain_order(p):
    """
    Matrix-Chain-Order given a list of integers corresponding to the dimensions
    of each pair of matrices forming a chain.

    :param list p: A list of integers.

    >>> M, S = matrix_chain_order([2, 20, 4, 6])
    >>> print(M)
    {(1, 1): 0, (2, 2): 0, (3, 3): 0, (1, 2): 160, (2, 3): 480, (1, 3): 208}
    >>> print(S)
    {(1, 2): 1, (2, 3): 2, (1, 3): 2}
    """
    s = {}
    m = {}
    n = len(p)

    for i in range(1, n):
        m[tuple([i, i])] = 0

    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            m[tuple([i, j])] = float('inf')
            for k in range(i, j):
                q = m[tuple([i, k])] + m[tuple([k + 1, j])] + (p[i - 1] * p[k] * p[j])
                if q < m[tuple([i, j])]:
                    m[tuple([i, j])] = q
                    s[tuple([i, j])] = k
    return m, s


def print_optimal_parens(s, i, j):
    """
    Print the optimal parentheses according to the S-matrix computed by the
    matrix_chain_order function.

    :param dict s: A dictionary of tuples corresponding to the minimum k
                   values from each step of ``matrix_chain_order``.
    :param int i: Starting index.
    :param int j: End index.

    Example (continued from previous function):

    >>> M, S = matrix_chain_order([2, 20, 4, 6])
    >>> print_optimal_parens(S, 1, 3)
    ((A_1A_2)A_3)

    General form:

    >>> chain = [2, 20, 4, 6]
    >>> M, S = matrix_chain_order(chain)
    >>> print_optimal_parens(S, 1, len(S) - 1)
    ((A_1A_2)A_3)
    """

    if i == j:
        print("A_{}".format(i), end='')
    else:
        print('(', end='')
        print_optimal_parens(s, i, s[tuple([i, j])])
        print_optimal_parens(s, s[tuple([i, j])] + 1, j)
        print(')', end='')


if __name__ == '__main__':

    # import argparse
    #
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-c',
    #                     '--chain',
    #                     default='30,35,15,5,10,20,25',
    #                     help='''Specify comma-separated integers for input.
    #                     [Default: 30,35,15,5,10,20,25]''')
    # parser.add_argument('-v',
    #                     '--verbose',
    #                     action='store_true',
    #                     help='Show the values of the S matrix.')
    #
    # args = parser.parse_args()
    # chain = [int(i) for i in args.chain.split(',')]
    chain = [30, 35, 35, 10, 15, 30, 30]
    m, s = matrix_chain_order(chain)

    # if args.verbose:
    for i, j in m:
        print('(i,j) = ({0},{1}): {2}'.format(i, j, m[tuple([i, j])]))

    print_optimal_parens(s, 1, len(chain) - 1)
    print()