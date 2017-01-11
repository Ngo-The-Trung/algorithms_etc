import sys

n = int(sys.stdin.read())

print n / 2
for i in range(n / 2 - 1):
    print 2,
if n % 2 == 0:
    print 2,
else:
    print 3,
