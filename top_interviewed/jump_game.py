# Author: Allen Anker
# Created by Allen Anker on 04/09/2018
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""


class Solution:
    def can_jump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        tail = len(nums) - 1
        # updating the closest index it needs to be able to reach
        can_reach = tail
        for i in range(tail, -1, -1):
            if nums[i] >= can_reach - i:
                can_reach = i

        return True if not can_reach else False


solution = Solution()
nums = [2, 3, 1, 1, 4]
print(solution.can_jump(nums))
