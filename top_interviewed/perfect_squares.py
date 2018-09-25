# Author: Allen Anker
# Created by Allen Anker on 25/09/2018
"""
Given a positive integer n, find the least number of
perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
"""
from math import sqrt


class Solution:
    _dp = [0]
    def num_squares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = self._dp
        while len(dp) <= n:
            # from the one just before the n, increments by 1 would be n
            dp += min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,
        return dp[n]


solution = Solution()
print(solution.num_squares(37))
