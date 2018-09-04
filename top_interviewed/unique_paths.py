# Author: Allen Anker
# Created by Allen Anker on 04/09/2018
"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?
"""
from math import factorial


class Solution:
    def unique_paths(self, m, n):
        """
        The steps to right and down is fixed to a certain grid.
        How many ways to insert the n-1 down steps into m-1 right steps.
        So, with some mathematics knowledge we learned in high school...
        :type m: int
        :type n: int
        :rtype: int
        """
        if m - 1 >= n:
            return int(self.comb(m + n - 2, n - 1))
        else:
            return int(self.comb(m + n - 2, m - 1))

    def comb(self, a, b):
        up = 1
        down = factorial(b)
        while b > 0:
            up *= a
            a -= 1
            b -= 1
        return up / down


solution = Solution()
print(solution.unique_paths(3, 2))
