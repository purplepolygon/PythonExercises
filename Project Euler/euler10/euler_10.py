#!/usr/bin/env python3
# Find the sum of all prime numbers below 2,000,000 NOT complete - need euler7
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


def array_of_n_number_of_primes_generator(limit):
    array_of_primes = [2, ]
    i = 2
    while i < limit:
        if prime_check(i):
            array_of_primes.append(i)
            i += 1
            continue
        else:
            i += 1
            continue
    return array_of_primes


def array_of_primes_sum(limit):
    array_of_primes = array_of_n_number_of_primes_generator(limit)
    i = 0
    prime_sum = 0
    for array_of_primes[i] in array_of_primes:
        prime_sum += array_of_primes[i]
        continue
    return prime_sum


if __name__ == "__main__":
    print(array_of_primes_sum(2000000))


# 142913828922
