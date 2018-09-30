# Author: Allen Anker
# Created by Allen Anker on 30/09/2018
"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""
from collections import deque


class Solution:
    def wiggle_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = len(nums) // 2 + 1 if len(nums) & 1 else len(nums) // 2
        left_half, right_half = deque(nums[:mid][::-1]), deque(nums[mid:][::-1])
        left = True
        for i in range(len(nums)):
            if left and i // 2 < mid:
                nums[i] = left_half.popleft()
                left = not left
            else:
                nums[i] = right_half.popleft()
                left = not left



solution = Solution()
nums = [4, 5, 5, 6]
solution.wiggle_sort(nums)
print(nums)
