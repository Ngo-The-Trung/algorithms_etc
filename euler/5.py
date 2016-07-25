#!/usr/bin/env python3
import math


primes = [2, 3, 5, 7, 11, 13, 17, 19]
pows = [4, 2, 1, 1, 1, 1, 1, 1]

t = 1
for i in range(len(primes)):
    t *= primes[i] ** pows[i]
print(t)
