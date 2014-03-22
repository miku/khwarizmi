#!/usr/bin/env python
# coding: utf-8

"""
Prefix averages.

Given a sequence of n numbers, compute another sequence A such that
A[j] is the average of elements S[0], .., S[j] for j = 0, .. n - 1.

Example, A = [2, 5, 3, 5], then S = [2, 3.5, 3.33, 3.75]
"""

from __future__ import division
from timer import Timer

def prefix_average_0(S):
    """ O(n^2) """
    A = []
    for j in range(1, len(S) + 1):
        A.append(sum(S[:j]) / j)
    return A


def prefix_average_10(S):
    """ Try something better. """
    # [2], 0 => 0 + (2 - 0) / (0 + 1)
    # [_ 5], 1 => 2 + (5 - 2) / (1 + 1) => 3.5
    # [_ _ 3], 2 => 3.5 + (3 - 3.5) / (2 + 1) => 3.33
    A, last = [], 0
    for i, s in enumerate(S, start=1):
        current = last + ((s - last) / i)
        A.append(current)
        last = current
    return A

def prefix_average_11(S):
    A, total = [], 0 # keep the total, stupid ...
    for i, s in enumerate(S, start=1):
        total += s
        A.append(total / i)
    return A


def prefix_average_1(S):
    """ O(n^2) from the book. """
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j + 1)
    return A

def prefix_average_2(S):
    """ From the book. Still O(n^2). """
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:j + 1]) / (j + 1)
    return A

def prefix_average_3(S):
    """ From the book, LT. """
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j + 1)
    return A


if __name__ == '__main__':
    A = [2, 5, 3, 5]
    A = range(10000)
    # print(A)
    
    with Timer() as timer:
        prefix_average_0(A)
    print(timer.elapsed_s)
    
    with Timer() as timer:
        prefix_average_10(A)
    print(timer.elapsed_s)

    with Timer() as timer:
        prefix_average_11(A)
    print(timer.elapsed_s)

    with Timer() as timer:
        prefix_average_1(A)
    print(timer.elapsed_s)

    with Timer() as timer:
        prefix_average_2(A)
    print(timer.elapsed_s)

    with Timer() as timer:
        prefix_average_3(A)
    print(timer.elapsed_s)
