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
        if len(nums) < 3:
            return
        length = len(nums)
        nums = sorted(nums)
        triplets = []
        for i in range(0, length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if i < length and j < length and nums[i] + nums[j] + nums[k] == 0:
                        triplet = [[nums[i], nums[j], nums[k]]]
                        triplets += triplet

        #remove duplicates in list
        triplets.sort()
        triplets = list(triplets for triplets,_ in itertools.groupby(triplets))
        return triplets


solution = Solution()
nums = [-1, 2, 1, -1, 0]
print(solution.threeSum(nums))
print(nums)