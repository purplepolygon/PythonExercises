#!/usr/bin/env python3
# In a list of numbers up to n, there are n-1 odd + 1 even number or there are n-1 even numbers + 1 odd numbers.
# Return the outlier: [2, 4, 0, 100, 39, 44] returns 39


def find_outlier(int_arr):
    checker = []
    """Get all even values, then check length of array."""
    for x in range(len(int_arr)):
        if int_arr[x] % 2 == 0:
            checker.append(int_arr[x])

    if len(checker) == len(int_arr) - 1:
        for x in range(len(int_arr)):
            if int_arr[x] % 2 == 1:
                return int_arr[x]

    elif len(checker) == 1:
        return checker[0]


# UPDATE - This logic and complexity can probably be optimized, I think this whole solution could probably be completely
# rewritten. Should I mark it ... to ... do? Eh, not worried about it. Perhaps later.


if __name__ == "__main__":
    print(find_outlier([2, 4, 0, 100, 39, 44]))  # 39
    print(find_outlier([37, 59, 100003, 97, 55, 22, 95, 101]))  # 22
