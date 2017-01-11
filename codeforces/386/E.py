import sys

lines = sys.stdin.read().splitlines()

n, m = [int(x) for x in lines[0].split(" ")]
_a = [int(x) for x in lines[1].split(" ")]
a = sorted(_a)

nodds = nevens = 0
for i in a:
    if i % 2 == 0:
        nevens += 1
    else:
        nodds += 1

odds = [0] * nodds
evens = [0] * nevens

iodds = ievens = 0

for i in a:
    if i % 2 == 0:
        evens[ievens] = i
        ievens += 1
    else:
        odds[iodds] = i
        iodds += 1

dups = 0

for i in range(1, len(a)):
    if a[i] == a[i-1]:
        dups += 1

print odds, evens, dups, m
if abs(nevens - nodds) % 2 != 0:
    print "-1"
else:
    print "TEST"
