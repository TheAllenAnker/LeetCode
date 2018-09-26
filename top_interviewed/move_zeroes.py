# Author: Allen Anker
# Created by Allen Anker on 26/09/2018
"""
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution:
    def move_zeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # records the position of "0"
        # move every non-zero forward, nums[zero] might not be zero
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1


solution = Solution()
nums = [1, 1, 0, 3, 0]
solution.move_zeroes(nums)
print(nums)
