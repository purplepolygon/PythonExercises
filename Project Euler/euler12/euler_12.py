#!usr/bin/env python3
# Triangle numbers: Created by adding set of natural numbers:
# 1 + 2 = 3,
# 1 + 2 + 3 = 6,
# 1 + 2 + 3 + 4 = 10
# First 3 triangle numbers: [3, 6, 10]
# Divisors for each:
# 3: 1, 3
# 6: 1, 2, 3, 6
# 10: 1, 2, 5, 10
# What is the first number that has over 500 divisors?
import math


def find_divisors(num):
    """ We use square root of a number as our ceiling as all divisors > sqrt(num) will be caught by
    it's sibling divisor that is < sqrt(num)"""
    divisors = []
    for x in range(1, int(math.sqrt(num)) + 1):
        if num % x == 0:
            divisors.append(x)
            if x * x != num:  # Find the corresponding divisor
                divisors.append(int(num / x))
    return divisors


def triangle_number_generator(number_of_factors):
    j = 2
    number = 3
    while len(find_divisors(number)) < number_of_factors:
        j += 1
        number += j
    return number


if __name__ == '__main__':
    #    print(triangle_number_generator(5))
    #       28
    print(triangle_number_generator(500))

# 76576500
