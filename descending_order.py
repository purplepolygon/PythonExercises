# Take any non-negative integer, return it's digits in descending order: '58901' -> '98510'


def descending_order(num):
    a = sorted(list(str(num)), reverse=True)
    b = int(''.join(map(str, a)))
    return int(b)
