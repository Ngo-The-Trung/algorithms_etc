#!/usr/bin/env python3


v1, v2 = 1, 2
s = 2

while True:
    v3 = v1 + v2
    if v3 > 4000000:
        break
    if v3 % 2 == 0:
        s += v3
    v1, v2 = v2, v3

print(s)
