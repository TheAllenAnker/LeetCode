# Author: Allen Anker
# Created by Allen Anker on 24/09/2018
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""


class Solution:
    def missing_number(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        i = 0
        while i < len(nums):
            if nums[i] != i:
                return i
            i += 1
        return len(nums)


solution = Solution()
nums = [0, 3, 1]
print(solution.missing_number(nums))
