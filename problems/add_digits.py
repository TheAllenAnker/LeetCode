# Author: Allen Anker
# Created by Allen Anker on 25/06/2018


"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
"""


import re


class Solution:
    def add_digit(self, num):
        """
        :type num: int
        :rtype: int
        """
        # a simple loop can solve this, but how does the following code work?
        # It is a variation of num % 9 but we don't want 0 as answer (when the num is 9).
        #  Now I am going to explain why num % 9 works.

        # if num >= 10 && num < 20, we can just calculate it by num - 9.
        #  We can verify it manually by enumerating all the numbers that num >= 10 && num < 20.
        #
        # if num >= 20 && num < 30, we can just calculate it by num - 9 * 2.
        #  We can verify it manually by enumerating all the numbers that num >= 20 && num < 30.
        # ...
        # Given a number abcdef, we can calculate it by num - 0 * f - 9 * e - 99 * d - 999 * c - 9999 * b - 99999 * a
        #
        # ....
        #
        # And we know the equation above is the same as num % 9 (but it never returns 0)

        if num == 0:
            return 0
        return 1 + (num - 1) % 9


solution = Solution()
print(solution.add_digit(38))