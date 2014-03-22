#!/usr/bin/env python
# coding: utf-8

"""
Pairwise swaps.
"""

from __future__ import print_function

def isort(l):
    for i in range(1, len(l)):
        key = l[i] # key keeps moving to the right
        for j in range(i - 1, -1, -1):
            # counting down
            if l[j] > l[j + 1]:
                l[j + 1], l[j] = l[j], l[j + 1]
            print(j + 1, j, l)


if __name__ == '__main__':
    isort([5, 2, 4, 6, 1, 3])

# 1 0 [2, 5, 4, 6, 1, 3]
# 2 1 [2, 4, 5, 6, 1, 3]
# 1 0 [2, 4, 5, 6, 1, 3]
# 3 2 [2, 4, 5, 6, 1, 3]
# 2 1 [2, 4, 5, 6, 1, 3]
# 1 0 [2, 4, 5, 6, 1, 3]
# 4 3 [2, 4, 5, 1, 6, 3]
# 3 2 [2, 4, 1, 5, 6, 3]
# 2 1 [2, 1, 4, 5, 6, 3]
# 1 0 [1, 2, 4, 5, 6, 3]
# 5 4 [1, 2, 4, 5, 3, 6]
# 4 3 [1, 2, 4, 3, 5, 6]
# 3 2 [1, 2, 3, 4, 5, 6]
# 2 1 [1, 2, 3, 4, 5, 6]
# 1 0 [1, 2, 3, 4, 5, 6]
