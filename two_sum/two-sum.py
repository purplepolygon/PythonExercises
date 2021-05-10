#!/usr/bin/env python3

class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            check = 0
            n = 1
            sol = []
            for x in nums:
                check = nums[x] + nums[x+n]
                if check == target:
                    sol = (nums[x], nums[x+n])
                    return sol
                elif n < len(nums) - x:
                    n += 1
                else:
                    break


print(twoSum([3,2,3], 6))
