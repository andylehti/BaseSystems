import string

def toBase(n, b):
    c = string.printable[:90]
    return '' if n == 0 else toBase(n // b, b) + c[n % b]

def fromBase(s, b):
    c = string.printable[:90]
    return sum(c.index(d) * b**i for i, d in enumerate(reversed(s)))
