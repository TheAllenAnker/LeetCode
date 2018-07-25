# Author: Allen Anker
# Created by Allen Anker on 24/07/2018
"""
Given a sorted array nums, remove the duplicates in-place
such that each element appear only once and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.
"""


class Solution:
    def remove_duplicates(self, nums):
        """
        :param nums: the array
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        if nums:
            last = nums[0]
            count += 1
            for i in range(1, len(nums)):
                if nums[i] != last:
                    last = nums[i]
                    count += 1

        return count


solution = Solution()
nums = [1, 2, 2, 2, 3, 3, 3]
print(solution.remove_duplicates(nums))