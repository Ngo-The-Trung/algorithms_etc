import sys
from collections import defaultdict
lines = sys.stdin.read().splitlines()
n = int(lines[0])

vals = [[int(x) for x in line.split(" ")] for line in lines[1:1 + n]]

last = defaultdict(list)

for i, t in enumerate(vals):
    a, b = t
    a -= 1
    last[a].append(i)

q = int(lines[1 + n])

def find_first(array, n):
    for i in range(len(array)):
        array[i] = n - array[i] - 1
    # print 'a', array
    for cursor in range(len(array)):
        target = array[cursor]
        # print cursor, target
        while target < len(array) and target != cursor:
            array[cursor] = array[target]
            next_ = array[target]
            array[target] = target
            target = next_
    # print array
    for i in range(len(array)):
        if i != array[i]:
            return n - i - 1
    return n - len(array) - 1

for i in range(q):
    quitters = [int(v) - 1 for v in lines[2 + n + i].split(" ")[1:]]
    pos = [last[quitter][-1] for quitter in quitters if len(last[quitter]) > 0]
    quitters = set(quitters)
    p = vals[find_first(pos, n)]
    r = p[0] - 1
    print r, last[r]
    best = p[1]
    for i in range(len(last[r]) - 1, -1, -1):
        for j in range(last[r][i] + 1, last[r][i+1]):
            v = vals[j]
            print v
