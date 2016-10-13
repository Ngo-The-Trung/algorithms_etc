#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

n_tests = int(lines[0])
cursor = 1

for test_number in range(n_tests):
    N, M = [int(v) for v in lines[cursor].split(" ")]
    roads = [[int(v) for v in text.split(" ")] for text in lines[cursor + 1:cursor + 1 + M]]
    cursor = cursor + M + 1

    road_counter = [0] * (N + 1)

    for road in roads:
        start, end = road
        road_counter[start] += 1
        road_counter[end] += 1
    print road_counter
    print sorted([sorted(tup) for tup in roads])
