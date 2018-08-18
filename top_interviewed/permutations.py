# Author: Allen Anker
# Created by Allen Anker on 17/08/2018
"""
Given a collection of distinct integers, return all possible permutations.
"""


class Solution:
    def permutations(self, nums):
        """
        Return all possible permutations.
        :param nums: Input number list
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permutations(nums[:i] + nums[i + 1:])] or [[]]
