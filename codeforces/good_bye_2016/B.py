import sys

lines = sys.stdin.read().splitlines()

p = 0
ok = True
for line in lines[1:]:
    a, b = line.split(" ")
    a = int(a)
    if p == 0 and b != "South":
        ok = False
        break
    if p == 20000 and b != "North":
        ok = False
        break
    if b == "North":
        p -= a
    elif b == "South":
        p += a
    if p > 20000 or p < 0:
        ok = False
        break

if ok and p == 0:
    print "YES"
else:
    print "NO"
