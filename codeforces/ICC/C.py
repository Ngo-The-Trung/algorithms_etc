#!/usr/bin/env python

import sys

lines = sys.stdin.read().splitlines()

N, M, K = [int(v) for v in lines[0].split(" ")]

corners = [(0, 0), (N, M), (N, 0), (0, M)]

reachable = {}
repeated = set()

dx, dy = 1, 1
cx, cy = 0, 0
time = 0

reachable[(0, 0)] = 0

while True:
    # print (dx, dy, cx, cy)
    if (dx, dy, cx, cy) in repeated:
        # print 'repeated'
        break

    repeated.add((dx, dy, cx, cy))

    # rem_X, rem_Y = (N - cx) * dx, (M - cy) * dy
    rem_X = (N - cx) if dx > 0 else cx
    rem_Y = (M - cy) if dy > 0 else cy
    # print "REM", rem_X, rem_Y
    if (rem_X > rem_Y):
        shift = rem_Y
        mx = 1
        my = -1
    else:
        shift = rem_X
        mx = -1
        my = 1

    for j in range(shift):
        time += 1
        cx += dx
        cy += dy
        # print (cx, cy)
        if (cx, cy) not in reachable:
            reachable[(cx, cy)] = time

    dx = mx * dx
    dy = my * dy

    if (cx, cy) in corners:
        # print "corner", (cx, cy)
        break

for i in range(K):
    x, y = [int(v) for v in lines[i + 1].split(" ")]
    if (x, y) in reachable:
        print reachable[(x, y)]
    else:
        print -1
