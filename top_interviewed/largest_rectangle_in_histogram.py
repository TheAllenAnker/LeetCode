# Author: Allen Anker
# Created by Allen Anker on 26/08/2018
"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.
"""


class Solution:
    def largest_rectangle_area(self, heights):
        """
        Find the largest rectangle area in histogram.
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        # stack maintains the indexes of heights in ascending order
        # so that we can calculate the area using a smaller height and bigger width
        # and compare it with the previous area we calculate
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans


solution = Solution()
heights = [2, 1, 5, 6, 2, 3]
print(solution.largest_rectangle_area(heights))
