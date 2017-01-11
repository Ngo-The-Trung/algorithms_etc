import sys
lines = sys.stdin.read().splitlines()

n, a, b = [int(x) for x in lines[0].split(" ")]
airports = [int(x) for x in lines[1]]
if airports[a-1] != airports[b-1]:
    print 1
else:
    print 0
