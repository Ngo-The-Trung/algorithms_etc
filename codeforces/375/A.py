#!/usr/bin/env python

# A. The new year: Meeting friends

import sys

def mid(X):
    left, m, right = sorted(X)
    return right - left


X = [int(v) for v in sys.stdin.read().split(" ")]
print mid(X)
