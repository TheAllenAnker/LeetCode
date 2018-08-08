# Author: Allen Anker
# Created by Allen Anker on 08/08/2018
"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""


class Solution:
    def search_insert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        l, r = 0, len(nums) - 1
        mid = 0
        while 0 <= l <= r < len(nums):
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if nums[mid] < target:
            mid = mid + 1
        return mid if mid != -1 else 0


solution = Solution()
nums = [1, 3, 5, 6, 7]
target = 2
print(solution.search_insert(nums, target))
