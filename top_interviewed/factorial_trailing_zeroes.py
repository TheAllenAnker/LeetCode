# Author: Allen Anker
# Created by Allen Anker on 13/09/2018
"""
Given an integer n, return the number of trailing zeroes in n!.
"""
from math import factorial


class Solution:
    def trailing_zeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n // 5 + self.trailing_zeroes(n // 5)


solution = Solution()
n = 30
print(solution.trailing_zeroes(n))
