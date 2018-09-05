# Author: Allen Anker
# Created by Allen Anker on 05/09/2018
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""
from math import factorial


class Solution:
    def climb_stairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climb_stairs(n - 1) + self.climb_stairs(n - 2)


solution = Solution()
print(solution.climb_stairs(6))
