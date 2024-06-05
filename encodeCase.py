import string

def getLetter(n, y=1): return string.ascii_letters[n] if y == 0 else ''.join(c for c in string.ascii_lowercase + ' ' if c)[n]

def dexBase(n, b, s):
    m = ""
    while s > 0: m, n, s = str(n % b) + " " + m if m else str(n % b), n // b, s - 1
    return f"{n} {m.rstrip()}"

def processString(n, s, y):
    parts = n.split()
    n, a = int(parts[0]), parts[1]
    a = getLetter(int(a), y)
    s += f'{a}'
    return n, s

def encodeCase(n):
    s = ''
    while True:
        if n < 52:
            break
        n, s = processString(dexBase(n, 52, 1), s, 0)
        while True:
            n, s = processString(dexBase(n, 27, 1), s, 1)
            if n < 52 or s[-1] == ' ':
                break
    s += getLetter(n, 0)
    return s

print(encodeCase(123456789))
