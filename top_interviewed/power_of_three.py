# Author: Allen Anker
# Created by Allen Anker on 30/09/2018
"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""


class Solution:
    def is_power_of_three(self, n):
        """
        Determine if a number is the power of three
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1162261467 % n == 0

