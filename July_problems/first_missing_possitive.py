# Author: Allen Anker
# Created by Allen Anker on 11/08/2018
"""
Given an unsorted integer array, find the smallest missing positive integer.
"""


class Solution:
    def first_missing_positive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums += [0]
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(n):
            nums[nums[i] % n] += n
        for i in range(1, n):
            if nums[i] // n == 0:
                return i
        return n


solution = Solution()
nums = [1, 2]
print(solution.first_missing_positive(nums))