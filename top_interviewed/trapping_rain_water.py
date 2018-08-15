# Author: Allen Anker
# Created by Allen Anker on 13/08/2018
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
"""


class Solution:
    def trap(self, height):
        """
        Find the minimum height than is greater than the current height from both sides.
        Then calculate the area.
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        ans = 0
        size = len(height)
        left_max, right_max = [0] * size, [0] * size
        left_max[0] = height[0]
        # highest on the left
        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i - 1])
        right_max[size - 1] = height[size - 1]
        # highest on the right
        for i in range(size - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])
        for i in range(1, size - 1):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans


solution = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(solution.trap(height))
