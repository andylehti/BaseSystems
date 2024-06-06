# note: this code needs gmpy2 installed
#  pip install gmpy2
# 1. this code is fairly large and inefficient. This code is minimally optimized. 

import gmpy2
from gmpy2 import mpz

def bConvert(n): # converts decimal value into a binary value which contains no consecutive 1 values.
    if n == 0: return '0'
    a, b, r = mpz(1), mpz(1), []
    while a + b <= n:
        a, b = a + b, a
    while a > 0:
        r.append('1' if n >= a else '0')
        if n >= a:
            n -= a
        a, b = b, a - b
    return ''.join(r).lstrip('0')[2:][:-1]

def deConvert(s):
    a, b, n, s = mpz(1), mpz(1), mpz(0), '10' + s + '0'
    for _ in range(len(s) - 2):
        a, b = a + b, a
    for c in s:
        if c == '1':
            n += a
        a, b = b, a - b
    return n

for i in range(100000):
    n = 10 + i
    e = bConvert(n)
    w = deConvert(e)
    print(f'{n} \t {e} \t {w} {n == w}')
