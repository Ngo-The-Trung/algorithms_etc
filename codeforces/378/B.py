import sys

buf = sys.stdin.readlines()
n = int(buf[0])
data = [[int(x) for x in line.split(" ")] for line in buf[1:1 + n]]

L = R = 0

for l, r in data:
    L += l
    R += r

B = abs(L - R)
m = B
best = 0

col = 1
for l, r in data:
    _L = L - l + r
    _R = R - r + l
    _B = abs(_L - _R)
    if _B > m:
        m = _B
        best = col
    col += 1

print best
