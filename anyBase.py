import math

def anyBase(n, b=1496):
    return '0' if n == 0 else ' '.join(str(n // b ** i % b) for i in range(int(math.log(n, b)), -1, -1))

def fromAnyBase(n, b=1496):
    return sum(int(c) * b ** i for i, c in enumerate(reversed(n.split(' '))))
