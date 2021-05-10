#!/usr/bin/env python3
# What is the 10,001st prime number? Not Complete
import math


def primenumberfinder():
    prime_list = [2]
    x = 8
    while len(prime_list) < 100:
        for i in range(2, int(x/2)):
            if x % i == 0:
                x += 1
                break
            else:
                prime_list.append(x)
                x += 1
                break
    return prime_list


print(primenumberfinder())
