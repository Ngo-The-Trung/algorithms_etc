import math
import sys

n, k = [int(x) for x in sys.stdin.read().split(" ")]

base = 240 - k
if base < 0:
    print 0
    sys.exit(0)

x = int(math.sqrt(base * 2 / 5))

s = x * (x + 1) * 5 / 2
if s > base:
    x -= 1
if x > n:
    x = n

print x
