# Author: Allen Anker
# Created by Allen Anker on 14/09/2018
"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        dummy = nums[len(nums) - k:] + nums[:len(nums) - k]
        for i in range(len(nums)):
            nums[i] = dummy[i]


solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution.rotate(nums, k)
print(nums)
