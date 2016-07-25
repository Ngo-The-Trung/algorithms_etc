#!/usr/bin/python3

primes = [2]
it = 1
count = 1
while True:
    it += 2

    is_prime = True
    for v in primes:
        if v * v > it:
            break
        if it % v == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(it)
        count += 1
        if count == 10001:
            break

print(primes[-1])
