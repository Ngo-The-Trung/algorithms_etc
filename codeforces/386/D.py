import sys

n, k, a, b = [int(x) for x in sys.stdin.read().split(" ")]
max_ = max(a, b)
min_ = min(a, b)

ngroups = 1 + (max_ - 1) / k

if min_ < ngroups - 1:
    print "NO"
else:
    if min_ == 0:
        if max_ > k:
            print "NO"
            sys.exit(0)

    if ngroups > 1:
        # print 'c', min_, ngroups
        k_ = min_ / (ngroups - 1)
        min_spill = min_ % (ngroups - 1)
        if k_ > k:
            # print 'b'
            k_ = min_ / ngroups
            min_spill = min_ % ngroups
    else:
        # print 'a'
        k_ = min_ / ngroups
        min_spill = min_ % ngroups
    # print k_, ngroups

    i = 0

    for _ in range(ngroups):
        for _ in range(min(k, max_)):
            if a > b:
                sys.stdout.write("G")
            else:
                sys.stdout.write("B")
        if min_spill > 0:
            r = min_spill
            min_spill = 0
        else:
            r = min(k_, min_)
        for _ in range(r):
            if a > b:
                sys.stdout.write("B")
                min_ -= 1
            else:
                sys.stdout.write("G")
                min_ -= 1
        max_ -= k
