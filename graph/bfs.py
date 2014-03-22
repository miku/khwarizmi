#!/usr/bin/env python
# coding: utf-8

"""
Depth-first search.

"""

# adjacency list
graph = {
    0: [1, 6, 8],
    1: [2, 3, 0],
    2: [10, 11],
    3: [1, 12, 4],
    4: [3, 13, 5],
    5: [4, 6, 9],
    6: [5, 7, 0],
    7: [6, 8, 9],
    8: [0, 7, 14],
    9: [5, 7, 15],
    10: [2],
    11: [2],
    12: [3],
    13: [4],
    14: [8],
    15: [9],
}

color = {}

def bfs(g, source):
    global color
    
    for v in g.iterkeys():
        color[v] = 'white'

    color[0] = 'black'

    queue = g[source]
    while len(queue) > 0:
        v = queue.pop(0)
        print('visiting %s (queued: %s)' % (v, len(queue)))
        color[v] = 'black'
        for neigbor in g[v]:
            if color[neigbor] == 'white' and not neigbor in queue:
                queue.append(neigbor)

if __name__ == '__main__':
    bfs(graph, 0)
