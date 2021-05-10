#!/usr/bin/env python3
# Find divisors (not including itself and 1) of a number and place it to a list


import math


def find_divisor(num):
    divisors = []
    for x in range(2, int(math.sqrt(num))):
        if num % x == 0:
            divisors.append(x)
            if x*x != num:
                divisors.append(int(num / x))

    if len(divisors) == 0:
        return str(num) + " is prime"

    else:
        divisors = sorted(divisors)
        return divisors


find_divisor(100)
