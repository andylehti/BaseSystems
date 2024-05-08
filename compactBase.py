import string
import numpy as np

def toBase(d, b):
    c, n, r = string.printable[:90], 1, d
    while r >= b ** n: r -= b ** n; n += 1
    s = ""
    while r > 0: s = c[r % b] + s; r //= b
    return s.zfill(n)

def fromBase(c, b): # converts any base that may contain leading zeroes to decimal to preserve the data
    chars = string.printable[:90]
    v, l = 0, len(c)
    for i, ch in enumerate(reversed(c)):
        v += chars.index(ch) * (b ** i)
    return v + sum(b ** i for i in range(1, l))
