import sys

lines = sys.stdin.read().splitlines()
x = [[int(x) for x in line.split(" ")] for line in lines ]

def f(a, b, c):
    return a[0] - b[0] + c[0], a[1] - b[1] + c[1]

x = set([f(x[0], x[1], x[2]), f(x[2], x[0], x[1]), f(x[1], x[2], x[0])])

print len(set(x))
for i in set(x):
    print i[0], i[1]
