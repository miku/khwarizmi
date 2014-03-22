#!/usr/bin/env python
# coding: utf-8

"""
Start with a single element list, which is sorted.
Then a two element list. "Move" elements in list to the right
to "make room" for the value. 
"""

#
# From the book
#
def sort(A):
    for i in range(len(A)):
        ins(A, i, A[i])

def ins(A, pos, value):
    i = pos - 1
    while i >= 0 and A[i] > value:
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = value


#
# Naive pythonic approach, even slower
#
def insert(A, value):
    """
    This is not as efficient as it could be, since
    we iterate over all values of a every time.
    """
    lower = [ a for a in A if a < value]
    upper = [ a for a in A if a >= value]
    return lower + [value] + upper

if __name__ == '__main__':
    A = [2, 6, 4, 7, 8, 1, 3, 2]

    # for i, value in enumerate(A):
    #     print(i, value, A)
    #     A = insert(A[:i], value)

    # print(A)


    sort(A)
    print(A)