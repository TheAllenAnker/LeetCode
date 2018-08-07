# Author: Allen Anker
# Created by Allen Anker on 07/08/2018
"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
"""


class Solution:
    def search_range(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find(nums, target, l, r):
            if not nums:
                return -1
            while 0 <= l <= r < len(nums):
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return  -1

        temp = find(nums, target, 0, len(nums) - 1)
        l = find(nums, target, 0, temp - 1)
        while l != -1:
            l_temp = l
            l = find(nums, target, 0, l - 1)
            if l == -1:
                l = l_temp
                break
        r = find(nums, target, temp + 1, len(nums) - 1)
        while r != -1:
            r_temp = r
            r = find(nums, target, r + 1, len(nums) - 1)
            if r == -1:
                r = r_temp
                break
        l = temp if l == -1 else l
        r = temp if r == -1 else r
        return [l, r]

solution = Solution()
nums = [1,1,1,1,1,1,2,3,4,4,5,5,5,6,7,8,8,8,8]
target = 5
print(solution.search_range(nums, target))
