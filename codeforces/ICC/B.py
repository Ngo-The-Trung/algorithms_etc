#!/usr/bin/env python

import sys

lines = sys.stdin.read().splitlines()

N, M = [int(v) for v in lines[0].split(" ")]

rows = []

for i in range(N):
    rows.append([int(v) for v in lines[i + 1].split(" ")])


oop = []

for i in range(N):
    oop.append(set())
    for j in range(M):
        if rows[i][j] != j + 1:
            tup = (rows[i][j], j + 1)
            oop[i].add(tup)
    if len(oop[i]) > 4:
        print "NO"
        sys.exit(0)

print oop
