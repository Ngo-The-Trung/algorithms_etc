import sys

lines = sys.stdin.read().splitlines()
s, x1, x2 = [int(x) for x in lines[0].split(" ")]
t1, t2 = [int(x) for x in lines[1].split(" ")]
p, d = [int(x) for x in lines[2].split(" ")]

if x1 > x2:
    x1 = s - x1
    x2 = s - x2
    p = s - p
    d = -d

walk_time = (x2 - x1) * t2
if x1 == x2:
    print 0
else:
    if d == -1:
        tram_path = p + x2
    else:
        if p <= x1:
            tram_path = (x2 - p)
        else:
            tram_path = (s - p) + s + x2

    train_time = tram_path * t1
    if train_time < walk_time:
        print train_time
    else:
        print walk_time
