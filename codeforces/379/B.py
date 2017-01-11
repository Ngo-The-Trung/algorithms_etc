#!/usr/bin/env python
import sys

k2, k3, k5, k6 = [int(v) for v in sys.stdin.read().split(" ")]

n256 = min(k2, k5, k6)
n32 = min(k3, k2 - n256)

print n256 * 256 + n32 * 32
