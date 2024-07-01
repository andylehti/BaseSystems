def toBaseArray(i):
    n, s, q = 1, 0, []
    while True:
        t = n**n
        if s + t > i: i -= s; break
        s += t; n += 1
    for j in range(n): q.append(str(i % n)); i //= n
    return ' '.join(q)

def checkArray(a): return all(x <= len(a) + 1 for x in a)

def fromBaseArray(s):
    s = list(map(int, s.split()))
    c, i = sum(j**j for j in range(1, len(s))), 0
    for v in reversed(s):
        i = i * len(s) + v
    return c + i if checkArray(s) == True else -1
