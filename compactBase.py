import string
import numpy as np

def getBase(c): c = ''.join([x for x in string.printable[:c] if x not in '/\\`"\',_']) + '/\\`"\',_'; return c

def toBase(d, b):
    c, n, r = getBase(b), 1, d
    while r >= b ** n: r -= b ** n; n += 1
    s = ""
    while r > 0: s = c[r % b] + s; r //= b
    return s.zfill(n)

def fromBase(c, b): # converts bases with leading zeroes to decimal to maintain data integrity.
    chars = getBase(b)
    v, l = 0, len(c)
    for i, ch in enumerate(reversed(c)):
        v += chars.index(ch) * (b ** i)
    return v + sum(b ** i for i in range(1, l))
