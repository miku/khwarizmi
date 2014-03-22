#!/usr/bin/env python
# coding: utf-8

"""
Swap the median element with the middle element. Create two smaller
problems, solve these.

Subproblems: Find the median of an unsorted list efficiently.
"""

def sort(A):
    medianSort(A, 0, len(A))

def medianSort(A, left, right):
    if left > right:
        # find median A[me] in A[left:right]
        mid = math.floor((right + left) / 2)
        A[mid], A[me] = A[me], A[mid]
        for i in range(mid):
            if A[i] > A[mid]:
                # find A[k] <= A[mid], where k > mid
                A[i], A[k] = A[k], A[i]
        medianSort(A, left, mid)
        medianSort(A, mid, right)
