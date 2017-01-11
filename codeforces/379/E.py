#!/usr/bin/env python
# TODO I think this is the right direction, but I failed the pretests

import sys

lines = sys.stdin.read().splitlines()
n = int(lines[0])

colors = [int(v) for v in lines[1].split(" ")]

adj = [None] * n

for i in range(n):
    adj[i] = []

for i in range(n - 1):
    u, v = [int(v) for v in lines[2 + i].split(" ")]
    u, v = u - 1, v - 1
    adj[u].append(v)
    adj[v].append(u)

blacks = whites = 0
visited = [False] * n

queue = [(0, 0)]
visited[0] = True
if colors[0] == 0:
    whites = 1
else:
    blacks = 1

regions_n = 0
regions = [[]]

while len(queue) > 0:
    top, region = queue.pop()
    for i in adj[top]:
        if not visited[i]:
            visited[i] = True
            new_region = region
            if colors[i] != colors[top]:
                new_region = regions_n + 1
                regions[region].append(new_region)
                regions.append([regions_n])
                regions_n = new_region

                if colors[i] == 0:
                    whites += 1
                else:
                    blacks += 1
            queue.append((i, new_region))

queue = [0]
visited = [False] * len(regions)
visited[0] = True
last = 0
while len(queue) > 0:
    top = queue.pop()
    for i in regions[top]:
        if not visited[i]:
            last = i
            visited[i] = True
            queue.append(i)

queue = [(last, 0)]
visited = [False] * len(regions)
visited[last] = True
last = 0
max = 0
while len(queue) > 0:
    top, dist = queue.pop()
    if dist > max:
        max = dist
    for i in regions[top]:
        if not visited[i]:
            visited[i] = True
            queue.append((i, dist + 1))

print max / 2
