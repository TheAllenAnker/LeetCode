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
                break

        # Find the "entrance" to the cycle.
        # One step at a time, they must meet in the entrance of the cycle
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1


solution = Solution()
nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
print(solution.find_duplicate(nums))
