# Author: Allen Anker
# Created by Allen Anker on 27/10/2018
"""
Write a function that takes a string as input and returns the string reversed.
"""


class Solution:
    def reverse_string(self, s):
        """
        Well, the solution is pretty straight forward in Python.
        :type s: str
        :rtype: str
        """
        return s[::-1]


solution = Solution()
print(solution.reverse_string("hello"))
