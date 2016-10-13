#!/usr/bin/env python

import sys

lines = sys.stdin.read().splitlines()

N, M = [int(v) for v in lines[0].split(" ")]
playlist = [int(v) for v in lines[1].split(" ")]

reps = N / M
counter = [0] * (M + 1)
changes = 0

for i in range(N):
    if playlist[i] <= M:
        counter[playlist[i]] += 1

for i in range(N):
    cur = playlist[i]
    if (cur <= M and counter[cur] > reps) or (cur > M):
        for v in range(1, M + 1):
            if counter[v] < reps:
                # print "Change", i, "from", playlist[i], "to", v
                if cur <= M:
                    counter[cur] -= 1
                counter[v] += 1
                playlist[i] = v
                changes += 1
                break

print reps, changes
print " ".join([str(x) for x in playlist])
