# Author: Allen Anker
# Created by Allen Anker on 23/09/2018
"""
Given an array nums, there is a sliding window of size k which is moving
from the very left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position. Return the max sliding window.

Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""
from collections import deque


class Solution:
    def max_sliding_window(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = deque()
        out = []
        for i, n in enumerate(nums):
            # the new number is larger than the current largest in the window
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            # the current leftmost falls out of the window
            if d[0] == i - k:
                d.popleft()
            # the number in the window is enough
            if i >= k - 1:
                out += nums[d[0]],
        return out
