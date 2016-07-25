#!/usr/bin/env python3


def is_palin(x):
    x = str(x)
    if x == x[::-1]:
        return True
    return False

m = -1
for i in range(100, 1000):
    for j in range(100, 1000):
        k = i * j
        if is_palin(k) and k > m:
            m = k

print(m)
