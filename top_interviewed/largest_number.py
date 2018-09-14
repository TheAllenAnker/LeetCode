# Author: Allen Anker
# Created by Allen Anker on 14/09/2018
"""
Given a list of non negative integers, arrange them such that they form the largest number.
"""


class LargerNumKey(str):
    # Combinations of descending order
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largest_number(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        # To avoiding returning a sequence of 0 when the array has only zeroes
        return '0' if largest_num[0] == '0' else largest_num