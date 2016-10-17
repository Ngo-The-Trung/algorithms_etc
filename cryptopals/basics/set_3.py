#!/usr/bin/env python

from lib import *
from collections import Counter
from string import ascii_lowercase, punctuation, whitespace


def rank(text):
    text = text.lower()
    pairs = sorted(Counter(text).items(), key=lambda x: -x[1])
    result = 0
    valid = ascii_lowercase + punctuation + whitespace
    for i, p in enumerate(pairs):
        c, f = p

        if c not in valid:
            result -= 10

        for it in frequency:
            _c, _f = it
            if _c == c:
                percent = f * 100.0 / len(text)
                if abs(percent / _f - 1.0) < 0.5:
                    result += 1
                break
    return result


def main():
    s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    h = s2h(s)
    l = len(s) / 2

    ranks = []
    for c in string.ascii_letters:
        _s = h2ascii(xor(h, [ord(c)] * l))
        count = 0
        for _c in _s:
            if _c in string.ascii_letters:
                count += 1
        if count > 10:
            ranks.append((c, _s, rank(_s)))

    for r in sorted(ranks, key=lambda x: x[2]):
        print r



if __name__ == "__main__":
    main()
