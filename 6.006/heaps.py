#!/usr/bin/env python
# coding: utf-8

"""
The cutest data structure.

E.g. for priority queues, and also sorting. Has unique properties.

PRIOQ: set of elements, each elements is associated with a *key*.

Is an ADT, with operations:

* insert(S, x)
* max(S)
* extract-max(S)
* increase-key(S, x, k)

Invariant: heap-property.

A heap is an implementation of a priority queue.

Basically an array, visualized as a nearly complete binary tree.

[16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

Heap as tree. Definition:

* root of the tree is the first element
* parent of i is i/2
* left(i) = 2i
* right(i) = 2i + 1

More types: max-heaps, min-heaps.

max-heaps: a key of a node is >= keys of the children.

max is trivial.

extract-max is not.
"""

