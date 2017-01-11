#!/usr/bin/env python
import sys

buf = sys.stdin.read().splitlines()
N = int(buf[0])
result = buf[1]
A = D = 0
for i in result:
    if i == "A":
        A += 1
    else:
        D += 1
print "Anton" if A > D else ("Danik" if D > A else "Friendship")
