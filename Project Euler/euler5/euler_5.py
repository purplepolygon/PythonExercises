#!/usr/bin/env python3
# Find smallest number divisible by all numbers 1-20
# Naive semi-optimized brute force math solution:
# Take 2520 (smallest number divisible by all numbers - 10
# Take all prime numbers from 11 - 20: 11, 13, 17, 19
# Multiply 2520 x 11 x 13 x 17 x 19 = 116396280 to get higher starting number for bruteforce
# Note that the starting number is divisible by 20, so we can increment +20


def divisibility_check(number):
    for y in range(1, 20):
        if number % y != 0:
            return False
    return True


def largest_divisible():
    x = 116396280
    while not divisibility_check(x):
        x += 20
    return x


print(largest_divisible())
