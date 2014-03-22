#!/usr/bin/env python

from collections import Counter
import random

# sample = [4, 6, 3, 7, 2, 7, 8, 9]
sample = [random.randint(0, 1000) for _ in range(10)]

def accumulator(start=0):
    """ A counter generator. Send the increment to this, and `None` to 
        print the sum of the sent in increments. """
    count = start
    while True:
        value = (yield)
        if value is None:
            yield count
            break
        else:
            count += value


def qsort(l, counter=None):
    counter.send(1)
    if len(l) <= 1:
        return l

    pivot, rest = l[0], l[1:]
    less, greater = [], []

    for item in rest:
        if item <= pivot:
            less.append(item)
        else:
            greater.append(item)

    return qsort(less, counter=counter) + [pivot] + qsort(greater, counter=counter)


if __name__ == '__main__':
    counter = accumulator()
    counter.send(None)    
    print(sample)
    print(qsort(sample, counter=counter))
    iterations = counter.send(None)
    print(iterations)