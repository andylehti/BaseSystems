import mpmath as mp

def anyBase(n, b=12): mp.mp.dps = len(str(n)) * 2; return [n // b ** i % b for i in range(int(mp.log(n, b)), -1, -1)]
def anyInverse(cn, b=12): mp.mp.dps = len(cn) * 2; return sum(d * b ** i for i, d in enumerate(reversed(cn)))
