# Author: Allen Anker
# Created by Allen Anker on 12/09/2018
"""
Given an integer array nums, find the contiguous sub-array
within the array (containing at least one number) which has the largest product.
"""


class Solution:
    def max_product(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        res = i_max = i_min = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                i_max, i_min = i_min, i_max
            i_max = max(nums[i], i_max * nums[i])
            i_min = min(nums[i], i_min * nums[i])

            res = max(res, i_max)
        return res


solution = Solution()
nums = [-2, 0, -1]
print(solution.max_product(nums))
