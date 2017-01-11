import sys

lines = sys.stdin.read().splitlines()
n = int(lines[0])
s = lines[1]

s1 = ""

if n % 2 == 0:
    s1 = s[0]
    s = s[1:]

for i, c in enumerate(s):
    if i % 2 == 0:
        s1 += c
    else:
        s1 = c + s1
print s1
