# Author: Allen Anker
# Created by Allen Anker on 13/09/2018
"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
from collections import defaultdict


class Solution:
    def majority_element(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution 1
        l = len(nums)
        count = defaultdict()
        for i in nums:
            if i in count:
                count[i] += 1
                if count[i] > l / 2:
                    return i
            else:
                count[i] = 1
        values = [key for key in count.keys() if count[key] > l / 2]
        return values[0]

    def majority_element2(self, nums):
        # solution 2
        nums.sort()
        return nums[len(nums) // 2]


solution = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
print(solution.majority_element(nums))
print(solution.majority_element2(nums))
