#!/usr/bin/env python
# coding: utf-8

"""
Simple vector class with some special methods.
"""

import math

class Vector(object):
    """ A list with vector addition. """
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, value):
        self._coords[j] = value

    def __add__(self, other):
        """ Vector addition. """
        if not len(self) == len(other):
            raise ValueError('Dimensions must agree.')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<%s>' % self._coords

    def __repr__(self):
        return '<%s>' % self._coords


class SequenceIterator(object):
    """ Mimic iteration. """
    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def next(self):
        self._k += 1
        if self._k < len(self._seq):
            return self, self._seq[self._k]
        else:
            raise StopIteration

    def __iter__(self):
        return self


class IterRange(object):
    """ A mock range via __iter__ and next (iterator protocol) """

    def __init__(self, start, stop=None, step=1):
        if step is 0:
            raise ValueError('Step must be > 0.')
        if stop is None:
            start, stop = 0, start
        self.stop = stop
        self.step = step
        self.i = start

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.stop:
            self.i = self.i + self.step
            return self.i
        else:
            raise StopIteration


class XRange(object):
    """ A mock range via __len__ and __getitem__ (what protocol?) """
    def __init__(self, start, stop=None, step=1):
        if step is 0:
            raise ValueError('Step must be > 0.')
        if stop is None:
            start, stop = 0, start
        self.start = start
        self.stop = stop
        self.step = step
        self.i = start

    def __len__(self):
        return (self.stop - self.start + self.step - 1) / self.step

    def __getitem__(self, j):
        if not 0 <= j < len(self):
            raise IndexError('Index out of range.')
        return self.start + self.step * j


class Progression(object):
    """ Base class for progressions. """

    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        """ Should be overridden by subclass. """
        self._current += 1

    def next(self):
        if self._current is None:
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print('%s' % ','.join((str(next(self)) for _ in range(n))))


class ArithmeticProgress(Progression):
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment


class GeometricProgress(Progression):
    def __init__(self, base=2, start=0):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self.base


class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super(FibonacciProgression, self).__init__(first)
        self.first = first
        self.second = second

    def _advance(self):
        self._current = self.first + self.second
        self.first, self.second = self.second, self._current


if __name__ == '__main__':
    # ### Vector
    # v = Vector(5)
    # v[1] = 23
    # u = v + v + range(5)
    # print(u, v)
    # print(sum(v))

    # ### Sequence mock
    # it = SequenceIterator(u)
    # for element in it:
    #     print(element)

    # ### Range thingy
    # print(len(XRange(8, stop=140, step=5)))
    # print(len(XRange(8)))

    # for i in XRange(8, 140, 5):
    #     print(i)

    # print('+')

    # for i in XRange(8, stop=140, step=5):
    #     print(i)

    # print(XRange(10)[9])

    # ### Progression
    fp = FibonacciProgression()
    fp.print_progression(20)