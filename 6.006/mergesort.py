#!/usr/bin/env python
# coding: utf-8

"""
Divide and conquer, with merge step O(n).

C + 2 * O(n/2) + C * n (merge)

(C * n) work in 1 + log n levels. Theta(n log n).
"""

def mergesort(array):
    """ 
    *very pretty algorithm*

    split the array in two parts, l, r

    and merge.
    """



def merge(l, r):
    """
    invariant: l' and r' are sorted
    *two finger algorithm*

    O(n)
    """
    merged = []
    left, right = 0, 0
    for _ in range(len(l) + len(r)):
        if l[left] <= r[right]:
            merged.append(l[left])
            left += 1
        else:
            merged.append(r[right])
            right += 1
    return merged


if __name__ == '__main__':
    x = merge([1, 5, 6], [2, 4, 7, 9])
    print(x)
