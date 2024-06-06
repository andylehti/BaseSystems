from functools import lru_cache
import string

def dexBase(n, b, s=1): # dex base is similar to the index base, however, the first value is the remainder of a base conversion that has stopped after s steps.
    m = ""
    while s > 0:
        m = str(n % b) + " " + m if m else str(n % b)
        n, s = n // b, s - 1
    return f'{n} {m}'

@lru_cache(maxsize=None)
def fromDexBase(s, b):
    r, *m = s.split(' ')
    return sum(int(d) * b ** i for i, d in enumerate(m[::-1])) + int(r) * (b ** len(m))

b = 2 # base index (uses symbol index for symbols instead of symbols for faster processing)
s = 3 # use as many as needed or wanted

for i in range(100000):
    n = 10 + i
    e = dexBase(n, b, s)
    w = fromDexBase(e, b)
    print(f'{n} \t {e} \t {w} {n == w}')
