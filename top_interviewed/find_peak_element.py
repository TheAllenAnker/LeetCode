# Author: Allen Anker
# Created by Allen Anker on 12/09/2018
"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.
"""


class Solution:
    def find_peak_element(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # A list is a combination of ascending or descending sequence of numbers
        # the peak is at the right of an ascending list or the left of a descending list
        if not nums:
            return
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return r


solution = Solution()
nums = [1, 2, 1, 3, 5, 6, 4]
print(solution.find_peak_element(nums))
