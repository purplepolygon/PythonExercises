#!/usr/bin/env python3
# Find divisors (not including itself and 1) of a number and place it to a list


import math


def find_divisors(num):
    """ We use square root of a number as our ceiling as all divisors > sqrt(num) will be caught by
    it's sibling divisor that is < sqrt(num)"""
    divisors = []
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            divisors.append(x)
            if x * x != num:  # Find the corresponding divisor
                divisors.append(int(num / x))

    if len(divisors) == 0:
        return print(str(num) + " is prime")
    else:
        divisors = sorted(divisors)
        print(divisors)
        return divisors


if __name__ == "__main__":
    # find_divisors(1)
    find_divisors(2)
    # find_divisors(3)
    find_divisors(4)
    # find_divisors(25)
    # find_divisors(100)  # [2, 4, 5, 20, 25, 50]
    # find_divisors(99)  # [3, 33]
    # find_divisors(117)  # [3, 9, 13, 39]
    # find_divisors(961)
    find_divisors(25)
