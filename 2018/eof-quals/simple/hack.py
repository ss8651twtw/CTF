#!/usr/bin/python3

magic = [0x47, 0xCD, 0x40, 0xC6, 0x7A, 0xD9, 0x45, 0xD9, 0x45, 0xAF, 0x2F, 0xAF, 0x50, 0xC0, 0x50, 0xFC]

x = 1
for i in magic:
    print(chr(i ^ x), end = '')
    x ^= 0x80