# Author: Allen Anker
# Created by Allen Anker on 15/09/2018
"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you
from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # A TLE solution...
        '''
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(nums[0] + self.rob(nums[2:]), nums[1] + self.rob(nums[3:]))
        '''
        pre, curr = 0, 0
        for i in nums:
            pre, curr = curr, max(pre + i, curr)
        return curr


solution = Solution()
nums = [2, 1, 1, 2]
print(solution.rob(nums))
