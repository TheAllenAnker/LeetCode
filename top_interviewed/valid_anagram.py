# Author: Allen Anker
# Created by Allen Anker on 24/09/2018
"""
Given two strings s and t , write a function to determine if t is an anagram of s.
"""


class Solution:
    def is_anagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


solution = Solution()
s = 'anagram'
t = 'aganram'
print(solution.is_anagram(s, t))
