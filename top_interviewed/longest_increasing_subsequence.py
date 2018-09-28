# Author: Allen Anker
# Created by Allen Anker on 28/09/2018
"""
Given an unsorted array of integers, find the length of longest increasing subsequence.
(It does not need to be consecutive.)

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""


class Solution:
    def length_of_LIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            max_dp = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_dp = max(max_dp, dp[j])
            dp[i] = max_dp + 1
        return max(dp)


solution = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(solution.length_of_LIS(nums))
