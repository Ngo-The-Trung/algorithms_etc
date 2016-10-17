#!/usr/bin/env python
from lib import *


def main():
    s1 = "1c0111001f010100061a024b53535009181c"
    s2 = "686974207468652062756c6c277320657965"
    s3 = "746865206b696420646f6e277420706c6179"
    assert h2s(xor(s2h(s1), s2h(s2))) == s3


if __name__ == "__main__":
    main()
