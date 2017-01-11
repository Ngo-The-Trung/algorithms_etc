#!/usr/bin/env python
import sys

lines = sys.stdin.read().splitlines()
n = int(lines[0])
x0, y0 = [int(v) for v in lines[1].split(" ")]

a = [0] * n

for i in range(n):
    line = lines[2 + i]
    t, x, y = line.split(" ")
    x, y = int(x), int(y)
    a[i] = (t, x, y)

max_val = 10 ** 9 + 1

directions = {
    (-1, -1): (False, max_val),
    (-1, 0): (False, max_val),
    (-1, 1): (False, max_val),
    (0, 1): (False, max_val),
    (1, 1): (False, max_val),
    (1, 0): (False, max_val),
    (1, -1): (False, max_val),
    (0, -1): (False, max_val)
}

for i in range(n):
    t, x, y = a[i]

    dx = abs(x0 - x)
    dy = abs(y0 - y)

    if (dx == dy) or dx == 0 or dy == 0:
        m = max(dx, dy)
        dx = ((x0 - x) / dx) if dx > 0 else 0
        dy = ((y0 - y) / dy) if dy > 0 else 0

        checked, distance = directions[(dx, dy)]

        # print m, distance, dx, dy
        if (m < distance):
            if dx == 0 or dy == 0:
                # print 'HU'
                # rook or queen
                if t in ['R', 'Q']:
                    directions[(dx, dy)] = (True, m)
                else:
                    directions[(dx, dy)] = (False, m)
            else:
                # bishop or queen
                if t in ['B', 'Q']:
                    directions[(dx, dy)] = (True, m)
                else:
                    directions[(dx, dy)] = (False, m)

for i in directions:
    checked, _ = directions[i]
    if checked == True:
        print "YES"
        sys.exit(0)
print "NO"
