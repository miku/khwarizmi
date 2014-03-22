#!/usr/bin/env python
# coding: utf-8

import random
import collections

def flatten(obj, collector=None):
    if collector is None:
        collector = []
    if isinstance(obj, collections.Iterable):
        for item in obj:
            flatten(item, collector=collector)
    else:
        collector.append(obj)
    return collector

def qsort(A):
    if len(A) <= 1:
        return A
    
    pidx = random.randint(0, len(A) - 1)
    pivot = A[pidx]
    A.pop(pidx)
    
    less, greater = [], []
    for element in A:
        if element <= pivot:
            less.append(element)
        else:
            greater.append(element)
    return [qsort(less), pivot, qsort(greater)]

if __name__ == '__main__':
    A = [1, 2, 3, 6, 8, 29, 12, 32]
    print(A)
    print(flatten(qsort(A)))
