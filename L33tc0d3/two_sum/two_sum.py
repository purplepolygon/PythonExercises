#!usr/bin/env python3
# Time: O(n) | Space: O(n)


def two_sum(nums, target):
    nums_dict = {}
    print(nums_dict)
    for i in range(len(nums)):
        if target - nums[i] in nums_dict:
            return [nums_dict[target - nums[i]], i]
        else:
            nums_dict[nums[i]] = i
            print(nums_dict)
            i += 1
            continue
    return []


print(two_sum([2, 7, 11, 15], 9))


if "__name__" == '__main__':
    print(two_sum([2, 7, 11, 15], 9))
