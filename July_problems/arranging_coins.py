# Author: Allen Anker
# Created by Allen Anker on 10/07/2018


"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.
"""


class Solution:
    def arrange_coins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # i = 0
        # while n > i:
        #     n -= i
        #     if n > i: i += 1
        # return i

        # solve the formula (n**2+n)/2 = Sn (arithmetic progression)
        return 0 if not n else int((n * 2 + 0.25) ** 0.5 - 0.5)


solution = Solution()
print(solution.arrange_coins(6))