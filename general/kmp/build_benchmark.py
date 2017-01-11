#!/usr/bin/python

import math
import random
import sys


def generate_suite_sizes(haystack_size):
    sizes = []
    L = haystack_size

    while L > 0:
        sizes.append((L, int(math.sqrt(haystack_size / L))))
        L /= 2

    sizes.reverse()

    return sizes


def main():
    if len(sys.argv) != 2:
        print "Usage: build_benchmark <text file>"
        sys.exit(1)

    text = open(sys.argv[1]).read()
    L = len(text)

    suites = []
    suite_sizes = generate_suite_sizes(L)
    for s in suite_sizes:
        needle_size, sample_size = s
        choices = random.sample(range(L - needle_size + 1), sample_size)
        for c in choices:
            suites.append(text[c:c+needle_size])
    print "\n".join(suites)


if __name__ == "__main__":
    main()
