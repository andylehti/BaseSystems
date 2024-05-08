import math

def anyBase(number, base=1496):
    return '0' if number == 0 else ' '.join(str(number // base ** i % base) for i in range(int(math.log(number, base)), -1, -1))

def fromAnyBase(converted_number, base=1496):
    return sum(int(digit) * base ** i for i, digit in enumerate(reversed(converted_number.split(' '))))
