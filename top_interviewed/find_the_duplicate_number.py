# Author: Allen Anker
# Created by Allen Anker on 26/09/2018
"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number,
find the duplicate one.

Note:
You must not modify the array (assume the array is read only). (So sorting is forbidden)
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""


class Solution:
    def find_duplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the intersection point of the two runners.
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                return tortoise


solution = Solution()
nums = [1, 2, 3, 3, 5, 4]
print(solution.find_duplicate(nums))
