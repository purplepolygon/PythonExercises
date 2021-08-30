#!/usr/bin/env python3
# Give the sum of all multiples of 3 and 5 under 5000


def solution(number):
    new_list = list(range(0, number))
    counter = 0
    for x in new_list:
        if x % 3 == 0 or x % 5 == 0:
            counter += x
    return counter


solution(5000)
