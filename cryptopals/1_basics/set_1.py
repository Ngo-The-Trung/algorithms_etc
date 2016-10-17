#!/usr/bin/env python
import string

base64_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"

def h2b(h):
    b = bin(h)[2:]
    return "0" * (8 - len(b)) + b

def s2h(s):
    return [int("0x" + s[i * 2:i * 2 + 2], 16) for i in range(len(s) / 2)]


def h264(h):
    # Ignore padding for now
    l = len(h) * 8 / 6
    result = ""
    for i in range(l):
        bits = i * 6
        byte_i = bits / 8
        start = bits % 8

        byte = h2b(h[byte_i])
        s = byte[start:start + 6]
        if len(s) < 6:
            byte = h2b(h[byte_i + 1])
            s += byte[:6 - len(s)]
        result += base64_chars[int("0b" + s, 2)]
    return result


def main():
    s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    assert h264(s2h(s)) == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

if __name__ == "__main__":
    main()
