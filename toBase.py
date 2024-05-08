import string

def getBase(c): c = ''.join([x for x in string.printable[:c] if x not in '/\\`"\',_']) + '/\\`"\',_'; return c

def toBase(n, b):
    c = getBase(b)
    return '' if n == 0 else toBase(n // b, b) + c[n % b]

def fromBase(s, b):
    c = getBase(b)
    return sum(c.index(d) * b**i for i, d in enumerate(reversed(s)))
