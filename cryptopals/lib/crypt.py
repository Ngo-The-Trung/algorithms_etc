import string

base64_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"


def h2b(h):
    b = bin(h)[2:]
    return "0" * (8 - len(b)) + b


def s2h(s):
    return [int("0x" + s[i * 2:i * 2 + 2], 16) for i in range(len(s) / 2)]


def h2s(h):
    return "".join([hex(v)[2:] for v in h])


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


def xor(h1, h2):
    l = len(h1)
    assert l == len(h2)

    return [h1[i] ^ h2[i] for i in range(l)]
