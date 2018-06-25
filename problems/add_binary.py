# Author: Allen Anker
# Created by Allen Anker on 25/06/2018


"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
"""


class Solution:
    def add_binary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = bin(int(a, 2) + int(b, 2))
        res = "" + res

        return res[2:]


solution = Solution()
print(solution.add_binary("10", "1000"))
