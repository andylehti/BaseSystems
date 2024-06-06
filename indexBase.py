def indexBase(r, b): # a mixture between anyBase, and compactBase; using an unconventional method of base conversion.
    o, r = [], r + 1
    while r > 0:
        c = (r % b) - 1
        if c < 0: c += b
        o.append(int(c)); r = (r - (c + 1)) // b
    return ' '.join(map(str, o[::-1]))

def fromIndexBase(s, b):
    s = s.split()
    n = len(s)
    r = sum((int(s[i]) + 1) * (b ** (n - 1 - i)) for i in range(n - 1))
    return r + int(s[-1])

b = 10 # change to any base

for i in range(100000):
    n = 10 + i
    e = indexBase(n, b)
    w = fromIndexBase(e, b)
    print(f'{n} \t {e} \t {w} {n == w}')
