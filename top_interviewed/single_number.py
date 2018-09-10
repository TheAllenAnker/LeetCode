# Author: Allen Anker
# Created by Allen Anker on 09/09/2018
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


class Solution:
    def single_number(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0, len(nums), 2):
            if i + 1 < len(nums):
                copy = nums[i]
                nums[i] = nums[i] - nums[i + 1]
            else:
                return nums[i]
            if nums[i] != 0:
                return copy


solution = Solution()
nums = [2, 2, 1, 1, 3, 5, 3]
print(solution.single_number(nums))
