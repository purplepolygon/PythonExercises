#!/usr/bin/env python3
# What is the 10,001st prime number?
import math


def prime_check(number):
    largest_factor = math.ceil((math.sqrt(number))) + 1
    list_of_potential_factors = [x for x in range(2, largest_factor)]
    i = 0
    for list_of_potential_factors[i] in list_of_potential_factors:
        if number % list_of_potential_factors[i] == 0:
            return False
        else:
            i += 1
            continue
    return True


# Prime checker tests
# assert(prime_check(7))
# assert(prime_check(113))
# assert(prime_check(160001))
# if prime_check(100):
#     assert()
# if prime_check(25):
#     assert()


def nth_prime_number(nth):
    array_of_primes = []
    i = 1
    while len(array_of_primes) < nth:
        if prime_check(i):
            array_of_primes.append(i)
            i += 1
            continue
        else:
            i += 1
            continue
    # print(array_of_primes[nth - 1])
    return array_of_primes[nth - 1]


if __name__ == "__main__":
    print(nth_prime_number(10))
    print(nth_prime_number(10001))

# 104743
