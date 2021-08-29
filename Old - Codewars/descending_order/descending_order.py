#!/usr/bin/env python3
# Take any non-negative integer, return it's digits in descending order: '58901' -> '98510'


def descending_order(num):
    sorted_array = sorted(list(str(num)), reverse=True)
    descending_integer = int(''.join(map(str, sorted_array)))
    print(descending_integer)
    return int(descending_integer)


if __name__ == '__main__':
    descending_order(58901)
    descending_order(11119)
    descending_order(4)
