def rotate(x: int):
    t = (x ^ (x >> 4)) & 0x00F0
    x = x ^ t ^ (t << 4)
    t = (x ^ (x >> 2)) & 0x0C0C
    x = x ^ t ^ (t << 2)
    return x

print(0b0000111100000000)
print(0b0100010001000100)

print(bin(rotate(0b0100010001000100)))