#!/usr/bin/env python
# coding: utf-8

"""
Given a list, find a peak element.

    [ ...a, b, c, ...]

    b >= a and b >= c
"""
from __future__ import print_function
import sys
import random
from timer import Timer

def linearpeaks(a):
    """ return all peak elements in a """
    # peaks = []
    for i, element in enumerate(a):
        print('.', end='')
        if i == 0:
            if a[i + 1] < a [i]:
                return a[i]
                # peaks.append((i, a[i]))
        elif i == len(a) - 1:
            if a[i - 1] < a [i]:
                return a[i]
                # peaks.append((i, a[i]))
        else:
            if a[i - 1] < a[i] > a[i + 1]:
                return a[i]
                # peaks.append((i, a[i]))
    return peaks


def fastpeaks(a):
    """ Only return "a" peak. """
    print('.', end='')
    if len(a) == 0:
        return None
    if len(a) == 1:
        return a[i]
    if len(a) == 2:
        return max(a)

    mid = len(a) // 2

    if mid == 0:
        if a[mid] > a[mid + 1]:
            return a[mid]
    elif mid == len(a) - 1:
        if a[mid - 1] < a[mid]:
            return a[mid]
    else:
        if a[mid - 1] < a[mid] > a[mid + 1]:
            return a[mid]
        if a[mid - 1] >= a[mid]:
            return fastpeaks(a[0:mid + 1])
        if a[mid + 1] >= a[mid]:
            return fastpeaks(a[mid:])



if __name__ == '__main__':
    with Timer() as timer:
        array = list(random.randint(0, 25) for _ in xrange(40))
    print(len(array), timer.elapsed_ms)
    print(array)

    with Timer() as timer:
        result = linearpeaks(array)
    print(result, timer.elapsed_ms)

    with Timer() as timer:
        result = fastpeaks(array)
    print(result, timer.elapsed_ms)

