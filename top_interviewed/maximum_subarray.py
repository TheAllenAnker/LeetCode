# Author: Allen Anker
# Created by Allen Anker on 03/09/2018
"""
Given an integer array nums, find the contiguous sub-array (containing at least one number)
which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.
"""


class Solution(object):
    def max_subarray(self, nums):
        """
        OK, this is a really brilliant solution I found online.
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


solution = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solution.max_subarray(nums))
