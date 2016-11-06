import sys

t1, t2, n = [int(v) for v in sys.stdin.read().split(" ")]
for i in range(n - 2):
    t1, t2 = t2, t1 + t2 * t2

print t2
