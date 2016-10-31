import sys
from collections import defaultdict

lines = sys.stdin.readlines()
n = int(lines[0])

data = [[int(v) for v in line.split(" ")] for line in lines[1:1+n]]

d = defaultdict(list)

counter = 0
for t in data:
    counter += 1
    a, b, c = sorted(t)

    alls = list(set([(a, b, c), (b, c, a), (a, c, b)]))
    for v in alls:
        a, b, c = v
        d[(a, b)].append((c, counter))

best = 0
best_p = best_p1 = best_p2 = 0
choice = 0

for t in d:
    l = d[t]
    a, b = t
    if len(l) == 1:
        c, pos = l[0]
        m = min(a, b, c)
        if m > best:
            choice = 1
            best = m
            best_p = pos
    else:
        l = sorted(l)
        c1, pos1 = l[-1]
        c2, pos2 = l[-2]
        c = c1 + c2
        m = min(a, b, c)
        if m > best:
            choice = 2
            best = m
            best_p1 = pos1
            best_p2 = pos2

if choice == 2:
    print 2
    print best_p1, best_p2
else:
    print 1
    print best_p
