# Author: Allen Anker
# Created by Allen Anker on 10/06/2018


"""
Given an array nums of n integers,
are there elements a, b, c in nums such that
 a + b + c = 0? Find all unique triplets
 in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

"""

import itertools


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 2): # 3 numbers are needed
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0: # sum is too small
                    l += 1
                elif s > 0: # sum is too large
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]: # remove duplicated triplets
                        l += 1
                    while l < r and nums[r] == nums[r - 1]: # remove duplicated triplets
                        r -= 1
                    l += 1
                    r -= 1
        return res


solution = Solution()
nums = [-1, 2, 1, -1, 0]
print(solution.threeSum(nums))
print(nums)
