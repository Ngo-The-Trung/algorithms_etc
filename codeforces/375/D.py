#!/usr/bin/env python

import sys
from copy import deepcopy

lines = sys.stdin.read().splitlines()
N, M, K = [int(v) for v in lines[0].split(" ")]

_map = [list(line) for line in lines[1:]]
old_map = deepcopy(_map)


def print_map(_map):
    for line in _map:
        print "".join(line)


def fill(x, y, symbol, replace):
    if _map[x][y] == symbol:
        return 0

    _map[x][y] = symbol
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    counter = 1
    for dx, dy in delta:
        n_x, n_y = x + dx, y + dy
        if 0 <= n_x < N and 0 <= n_y < M:
            if _map[n_x][n_y] == replace:
                counter += fill(n_x, n_y, symbol, replace)
    return counter


def cover_edges():
    for i in range(N):
        fill(i, 0, "*", ".")
        fill(i, M - 1, "*", ".")

    for i in range(M):
        fill(0, i, "*", ".")
        fill(N - 1, i, "*", ".")

def find_lakes():
    lakes = []
    for i in range(N):
        for j in range(M):
            if _map[i][j] == ".":
                size = fill(i, j, "?", ".")
                lakes.append((i, j, size))
    return lakes


cover_edges()
lakes = sorted(find_lakes(), key = lambda x : x[2])
_map = old_map
counter = 0
for i in range(len(lakes) - K):
    x, y, size = lakes[i]
    counter += size
    fill(x, y, "*", ".")
print counter
print_map(_map)
