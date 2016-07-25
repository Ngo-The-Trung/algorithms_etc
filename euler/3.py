#!/usr/bin/env python3
import math


X = 600851475143
m = math.floor(math.sqrt(X))
primes = [2]
it = 1
while True:
    it += 2
    if it > m:
        break

    is_prime = True
    for v in primes:
        if v * v > it:
            break
        if it % v == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(it)

for v in primes[::-1]:
    if X % v == 0:
        print(v)
        break
