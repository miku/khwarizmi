#!/usr/bin/env python
# coding: utf-8

"""
3-way set disjointness.
"""

from __future__ import division
from timer import Timer
import random


def naive(A, B, C):
    """ a * b * c """
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True

def better(A, B, C):
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == b == c:
                        return False
    return True

def disjoint(A, B, C):
    return len(A.union(B).union(C)) == (len(A) + len(B) + len(C))

if __name__ == '__main__':
    pool = range(1000000)
    A = set(random.sample(pool, 200))
    B = set(random.sample(pool, 200))
    C = set(random.sample(pool, 200))

    with Timer() as timer:
        naive(A, B, C)
    print(timer.elapsed_s)

    with Timer() as timer:
        better(A, B, C)
    print(timer.elapsed_s)

    with Timer() as timer:
        disjoint(A, B, C)
    print(timer.elapsed_s)
