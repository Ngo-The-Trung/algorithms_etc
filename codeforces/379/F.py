#!/usr/bin/env python
import sys

# (a and b) + (a or b) = (a + b)
lines = sys.stdin.read().splitlines()
n = int(lines[0])
b = [int(v) for v in lines[1].split(" ")]
c = [int(v) for v in lines[2].split(" ")]

s = sum(b) + sum(c)
if s % (n * 2) != 0:
    print -1
else:
    v = s / (n * 2)
    a = [0] * n
    result = True
    for i in range(n):
        if b[i] + c[i] < v:
            print i, b[i], c[i], v
            result = False
            break
        a[i] = ((b[i] + c[i]) - v) / n
    if not result:
        print -1
    else:
        for i in range(n):
            print a[i],
