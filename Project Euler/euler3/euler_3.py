#!/usr/bin/env python3
# Find the largest prime factor of n, n = 600851475143


import math


def largest_prime(n):
    for x in range(2, int(math.sqrt(n)) + 1):
        while n % x == 0:
            n = n / x
            if n == 1 or n == x:
                print(x)
                break


largest_prime(600851475143)

