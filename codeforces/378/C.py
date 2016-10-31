import sys
lines = sys.stdin.readlines()

n = int(lines[0])
k = int(lines[2])
init = [int(v) for v in lines[1].split(" ")]
final = [int(v) for v in lines[3].split(" ")]

sum_init = sum(init)
sum_final = sum(final)
if sum_init != sum_final:
    print "NO"
    sys.exit(0)

def test(start, end):
    if end - 1 == start:
        return ""

    m = start
    dire = None
    found = False
    for i in range(start, end):
        left = right = True
        if i < end - 1:
            if init[i + 1] >= init[i]:
                right = False
        if i != start:
            if init[i - 1] >= init[i]:
                left = False
        if (left or right) and init[i] > init[m]:
            found = True
            m = i
            dire = "L" if left else right

    if not found:
        return None

    pattern = [0] * (end - start)
    if dire == "L":
        pattern[0] = (m, "L")
        m -= 1
        end -= 1
    else:
        pattern[0] = (m, "R")
        end -= 1

    for i in range(end - m):
        # print i
        pattern[1 + i] = (m, "R")
    for i in range(m - start):
        # print i
        pattern[1 + end - m + i] = (m - i - 1, "L")

    return pattern

s = 0
j = 0
start = 0
order = []
for i in range(len(init)):
    s += init[i]
    if s > final[j]:
        print "NO"
        sys.exit(0)
    if s == final[j]:
        j += 1
        v = test(start, i + 1)
        if not v:
            print "NO"
            sys.exit(0)
        order.append(v)
        start = i + 1
        s = 0
print "YES"
for k in order[::-1]:
    for t in k:
        print t[0] + 1, t[1]
