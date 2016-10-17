import string

base64_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
frequency = [
    ("e", 12.702),
    ("t", 9.056),
    ("a", 8.167),
    ("o", 7.507),
    ("i", 6.966),
    ("n", 6.749),
    ("s", 6.327),
    ("h", 6.094),
    ("r", 5.987),
    ("d", 4.253),
    ("l", 4.025),
    ("c", 2.782),
    ("u", 2.758),
    ("m", 2.406),
    ("w", 2.360),
    ("f", 2.228),
    ("g", 2.015),
    ("y", 1.974),
    ("p", 1.929),
    ("b", 1.492),
    ("v", 0.978),
    ("k", 0.772),
    ("j", 0.153),
    ("x", 0.150),
    ("q", 0.095),
    ("z", 0.074)
]


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


def h2ascii(h):
    return "".join([chr(v) for v in h])


def xor(h1, h2):
    l = len(h1)
    assert l == len(h2)

    return [h1[i] ^ h2[i] for i in range(l)]
