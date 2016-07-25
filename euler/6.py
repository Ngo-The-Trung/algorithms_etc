#!/usr/bin/python3

print(sum(i + 1 for i in range(100))**2 - sum((i + 1) ** 2 for i in range(100)))
