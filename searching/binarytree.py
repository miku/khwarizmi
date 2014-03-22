#!/usr/bin/env python
# coding: utf-8

"""
Binary tree search.

Dynamic search sets. Binary search is ok for static lists, but if elements
change constantly, a tree is better suited.

Binary tree, at most two leaves per node, variations are B-trees with
n children per node.

Binary search trees perform well with dynamic data where insertions and
deletions are frequent.

"binary-search-tree property" (Cormen)

A binary tree is analogous to a precomputed "find the number game".

Balanced trees avoid degenerate cases, where tree become lists.

There are two popular balanced trees: AVL (Adel'son, Vel'skii, Landis, 1962) and
Red-black trees.

RBTrees garantuee that no branch has the height of two times that of any other
branch.

An RBTree satisfies the following conditions:

* every node is labeled either red or black
* the root is black
* every leaf node contains a null value and is black
* all red nodes have two black children
* every simple path from one node to one of its decendant leaf nodes
  contains the same number of black nodes

On insertion (deletion) the RB properties might be violated, so:

"The fundamental operation when restructuring the tree is a rotation about a
node."



"""
