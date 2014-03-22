#!/usr/bin/env python
# coding: utf-8

"""
2d version of peak finding.

http://en.wikipedia.org/wiki/Hill_climbing

Given a matrix. n rows, m columns. A peak is a hill.

x x c x x
x b a d x
x x e x x

a is 2d peak, iff a >= b, a >= d, a >= c, a >= e

Greedy ascent algorithm.

Theta(mn) complexity. Or Theta(n^2) if m == n.
"""

import random
import pprint

def naive():
    """
    - pick middle column j = m // 2
    - find a 1d peak at (i, j)
    - use (i, j) as a start to find a 1d peak on row i

    efficient, but INCORRECT!

    - a 2d peak might not exist on row i!
    """
    pass

def hillclimber(matrix):
    """
    - pick middle column j = m // 2
    - find global max in col j at (i, j)
    - compare (i, j - 1), (i, j), (i, j+ 1)
    - pick left cols if (i, j - 1) > (i, j)
    - if (i, j) >= (i, j - 1), (i, j + 1) => (i, j) is a 2d peak
    - solve new problem with half the number of columns
    - if you have a single col, find global max and be done (base case)
    """
    j = len(matrix[0]) // 2
    # maxvalue is the global max in column j
    # rowmax is the row index of the maximum
    maxvalue, rowmax = -1, -1
    for row in range(len(matrix)):
        if maxvalue <= matrix[row][j]:
            maxvalue = matrix[row][j]
            rowmax = row
    print(rowmax, j, maxvalue)
    left, right = 0, 0
    if j > 0:
        left = matrix[rowmax][j - 1]
    if j < len(matrix[0]) - 1:
        right = matrix[rowmax][j + 1]
    if left <= maxvalue >= right:
        return (rowmax, j, maxvalue)
    if left > maxvalue:
        half = []
        for row in matrix:
            half.append(row[:j + 1])
        return hillclimber(half)
    if right > maxvalue:
        half = []
        for row in matrix:
            half.append(row[j:])
        return hillclimber(half)



def genmatrix(n=7, m=7, lower=0, upper=9):
    return [[random.randint(lower, upper) for _ in range(m)] for _ in range(n)]


if __name__ == '__main__':
    matrix = genmatrix(upper=9)
    pprint.pprint(matrix)
    hillclimber(matrix)