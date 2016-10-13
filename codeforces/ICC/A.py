#!/usr/bin/env python

import sys

days = [v % 7 for v in [28, 30, 31]]

dow = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

a, b = sys.stdin.read().splitlines()

diff = dow.index(b) - dow.index(a)

if diff < 0:
    diff += 7
if diff in days:
    print "YES"
else:
    print "NO"
