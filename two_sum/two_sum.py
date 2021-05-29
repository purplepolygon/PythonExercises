#!/usr/bin/env python3


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


if __name__ == '__main__':
    print(two_sum([3, 2, 3, 7, 15, 22, 9, 8], 17))
