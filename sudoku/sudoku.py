#!/usr/bin/env python
# coding: utf-8

import random
import itertools


def nonoverlapping(p, q):
    """ Return true, if p and q share no element at the same position. """
    # if not len(p) == len(q):
    #     raise ValueError('permutations must be of same length')
    return all([ p != q for p, q in zip(p, q)])


def sudoku_board(size=9):
    """ Naive and slow version. """
    permutations = list(itertools.permutations(range(1, size + 1)))
    print(len(permutations))
    rows = [random.choice(permutations)]
    while len(rows) < size:
        print_board(rows)
        print('-' * 24)
        for p in permutations:
            if all([nonoverlapping(p, row) for row in rows]):
                rows.append(p)
                break
            else:
                continue
            break
    return rows


def print_board(board):
    for row in board:
        print(row)


def sudoku_random(size):
    """
    Generate a random sudoku of dimension size x size.

    * Generate permutations of range(1, size + 1).

    This fails, because it is not enough to consider
    just a single set of candidates. Intuitively one might think of backtracking,
    until a valid board is found.
    """
    material = set(range(1, size + 1))
    board = [[0 for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            print(board)
            taken_in_row = board[i][:j]
            taken_in_column = [row[j] for row in board]
            taken = set(taken_in_row).union(taken_in_column)
            candidates = material.difference(taken)
            board[i][j] = candidates.pop()
            print(i, j, candidates)

if __name__ == '__main__':
    # sudoku_board()
    # print(nonoverlapping([2, 3, 1], [1, 2, 3]))
    board = sudoku_board()
    print_board(board)
