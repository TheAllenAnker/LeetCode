# Author: Allen Anker
# Created by Allen Anker on 18/07/2018


"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


class Solution:
    def max_area(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        max_area, l, r = 0, 0, length - 1
        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            # in each iteration, either a row or a column in a matrix is eliminated
            # if we see l side of the container as row value of a matrix, and the right side is the column
            if height[r] >= height[l]:
                l += 1
            else:
                r -= 1

        return max_area


solution = Solution()
height = [1, 1, 2, 1, 1, 1, 2]
print(solution.max_area(height))