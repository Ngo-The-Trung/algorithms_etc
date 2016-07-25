#!/usr/bin/env python3


def s(n):
    amount = 999 // n
    return n * amount * (amount + 1) // 2


print(s(3) + s(5) - s(15))
