# Author: Allen Anker
# Created by Allen Anker on 20/09/2018
"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""
from collections import defaultdict


class Solution:
    def contains_duplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = defaultdict()
        for i in nums:
            if seen.get(i):
                return True
            else:
                seen[i] = 1
        return False


solution = Solution()
nums = [1, 2, 3]
print(solution.contains_duplicate(nums))
