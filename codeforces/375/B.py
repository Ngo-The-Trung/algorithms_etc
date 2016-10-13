#!/usr/bin/env python

import sys

N, S = sys.stdin.read().splitlines()
N = int(N)

inside = False
max_len_out = 0
count_in = 0
current = 0

S = S + "_"

for c in S:
    if c == "(":
        inside = True
        if current > max_len_out:
            max_len_out = current
        current = 0
    elif c == ")":
        inside = False
        if current > 0:
            count_in += 1
            current = 0
    elif c == "_":
        if current > 0:
            if inside:
                count_in += 1
            else:
                if current > max_len_out:
                    max_len_out = current
            current = 0
    else:
        current += 1

print max_len_out, count_in
