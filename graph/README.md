README
======

Graphs:

* directed, undirected, weighted
* Hypergraphs (multiple edges between same nodes)

Connected graph.

Representation of a graph with n vertices: n adjacency list, each node maintains
a list of node it is connected to. Or n x n adjacency matrix.

Sparse graphs are better represented with lists. E.g. airline flights between
cities. 1659 airports worldwide, 71M aircraft movements, or 200K flights per
day. But the number of combinations 1659^2 >> 200K flights, and these flights
may not be between unique locations. Example of a sparse matrix.


