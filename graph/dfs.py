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

source = 0
target = 15

d = f = pred = color = {}
counter = 0

def dfs(g, s):
    global color
    for v in g.keys():
        color[v] = 'white'
    dfs_visit(s)

    print('visiting other compontents...')
    for v in g.keys():
        if color[v] == 'white':
            dfs_visit(v)

def dfs_visit(u):
    print('visiting %s' % u)
    global color
    color[u] = 'gray'
    for neigbor in graph[u]:
        if color[neigbor] == 'white':
            dfs_visit(neigbor)
    color[u] = 'black'

if __name__ == '__main__':
    dfs(graph, 0)
