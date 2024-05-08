# additional functions to process strings of numbers separated by numbers all at once, i.e. convertBase('2154 53656 63 7434 2456', 32) -> convertDecimal('23a 1kco 1v 78a 2co', 32) -> '2154 53656 63 7434 2456'

def convertBase(a, b):
    c = a.split()
    d = [toBase(int(e), b) for e in c]
    return ' '.join(d)

def convertDecimal(a, b):
    c = a.split()
    d = [fromBase(e, b) for e in c]
    return ' '.join(map(str, d))
