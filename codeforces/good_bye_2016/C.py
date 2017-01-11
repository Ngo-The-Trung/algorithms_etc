import sys

lines = sys.stdin.read().splitlines()[1:]

mini = None
maxi = None

def add(a, b):
    if a == "+inf" or a == "-inf":
        return a
    return a + b

def gt(a, b):
    if a == "+inf":
        return True
    return a > b

def lt(a, b):
    if a == "-inf":
        return True
    return a < b

prev = None
for line in lines:
    c, d = [int(x) for x in line.split(" ")]

    if prev is None:
        if d == 1:
            mini = 1900
            maxi = "+inf"
        else:
            mini = "-inf"
            maxi = 1899
    else:
        if d == 2:
            if gt(maxi, 1899):
                maxi = 1899
        else:
            if lt(mini, 1900):
                mini = 1900

        if not gt(maxi, mini):
            print "Impossible"
            sys.exit(0)

    mini = add(mini, c)
    maxi = add(maxi, c)

    prev = d

if maxi == "+inf":
    print "Infinity"
else:
    print maxi
