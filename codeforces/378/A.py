import sys

vowels = "AEIOU"

s = sys.stdin.read().strip() + "E"
p = -1
m = 1
for i in range(len(s)):
    if s[i] in vowels:
        if m < i - p:
            m = i - p
        p = i

print m
