def toMultiBase(n):
    r, b = [], 1
    while n > 0:
        r.append((n % b) + 1)
        n //= b
        b += 1
    return ' '.join(map(str, r))

def fromMultiBase(vs):
    vs, n, p, b = list(map(lambda x: x-1, map(int, vs.split()))), 0, 1, 1
    for v in vs:
        n += v * p
        p *= b
        b += 1
    return n

# for i in range(1, 10000):
#    a = toMultiBase(i)
#    b = fromMultiBase(a)
#    print(f'{i} = {a} \t = {b}  \t{b == i}')
# test using the above code snippet
