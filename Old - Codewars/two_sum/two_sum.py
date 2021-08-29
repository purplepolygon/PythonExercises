#!/usr/bin/env python3
# What does this do? Finds two numbers in an array that add up to the target number.
# Example: [1, 3, 5, 9], 10, would be 0, 3  as 1 + 9 = 10.


def two_sum(nums, target):
    for x in range(0, len(nums) - 1):
        n = 1
        while n < len(nums) - x:
            check = nums[x] + nums[x + n]
            if check == target:
                return [x, x + n]
            else:
                n += 1
                continue
    raise Exception("No two numbers in this array add up to the target")


if __name__ == '__main__':
    print(two_sum([3, 2, 3, 7, 15, 22, 9, 8], 37))  # [4, 5]
    print(two_sum([3, 2, 3, 7, 15, 22, 9, 8], 17))  # [4, 5]
    print(two_sum([3, 2, 3, 7, 15, 22, 9, 8], 77))  # Error
