import sys

a, b, c = [int(x) for x in sys.stdin.read().splitlines()]

c /= 4
b /= 2

a = min(a, b, c)
print a + a * 2 + a * 4
