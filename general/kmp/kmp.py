#!/usr/bin/env python

# http://www.ics.uci.edu/~eppstein/161/960227.html


def search(haystack, needle):
    fallback = [0] * len(needle)
    fallback[0] = -1

    ci = 0  # candidate index
    for i in range(1, len(needle)):
        if needle[i] == needle[ci]:
            fallback[i] = ci
            ci += 1
        elif ci > 0:
            ci = fallback[ci]
            i -= 1

        print i, ci

    print fallback
    i = ci = 0
    while i + ci < len(haystack):
        print i + ci, ci, haystack[i + ci], needle[ci]
        if haystack[i + ci] == needle[ci]:
            print 'next'
            ci += 1
            if ci == len(needle):
                return True
        elif fallback[ci] > -1:
            print 'fallback'
            i = i + ci - fallback[ci]
            ci = fallback[ci]
        else:
            print 'reset'
            i += 1
            ci = 0
    return False


print search("a" * 4 + "b" + "a" * 5, "a" * 5)
