import sys
n, k = [int(x) for x in sys.stdin.read().split(" ")]

size = 1
sizes = [1]
l = 1
while size < k:
    size = size * 2 + 1
    sizes.append(size)
    l += 1
while l > 0:
    l -= 1
    size = sizes[l]
    if size < k - 1:
        k -= size + 1
    elif size == k - 1:
        print l + 2
        break
    elif size == k:
        print 1
        break
